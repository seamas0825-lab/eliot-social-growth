#!/usr/bin/env node
// Web Access CDP proxy smoke test using a temporary Chrome profile.

import { spawn } from 'node:child_process';
import { mkdtemp, readFile, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';

function arg(name, fallback = null) {
  const i = process.argv.indexOf(name);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const webAccessDir = arg('--web-access-dir');
const chromePath = arg('--chrome-path', process.platform === 'darwin'
  ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
  : process.platform === 'win32'
    ? 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    : 'google-chrome');
const launchChrome = process.argv.includes('--launch-chrome');
if (!webAccessDir) {
  console.error(JSON.stringify({ ok: false, adapter: 'web-access', error: '--web-access-dir is required' }));
  process.exit(2);
}

const proxyPort = String(34000 + Math.floor(Math.random() * 1000));
let debugPort = '0';
const profile = await mkdtemp(path.join(os.tmpdir(), 'web-access-smoke-'));
const browserProfileDir = process.platform === 'darwin'
  ? path.join(profile, 'Library', 'Application Support', 'Google', 'Chrome')
  : process.platform === 'win32'
    ? path.join(profile, 'Google', 'Chrome', 'User Data')
    : path.join(profile, '.config', 'google-chrome');
let browser = null;
let proxy = null;
let targetId = null;

const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
async function jsonFetch(url, options = {}) {
  const response = await fetch(url, { ...options, signal: AbortSignal.timeout(10000) });
  const body = await response.text();
  let parsed;
  try { parsed = JSON.parse(body); } catch { parsed = { raw: body }; }
  if (!response.ok || parsed.error) throw new Error(parsed.error || `HTTP ${response.status}`);
  return parsed;
}

try {
  if (launchChrome) {
    browser = spawn(chromePath, [
      '--remote-debugging-port=0',
      `--user-data-dir=${browserProfileDir}`,
      '--headless=new',
      '--no-first-run',
      '--no-default-browser-check',
      'about:blank',
    ], { stdio: 'ignore' });
    const activePortFile = path.join(browserProfileDir, 'DevToolsActivePort');
    for (let i = 0; i < 30; i++) {
      try {
        debugPort = (await readFile(activePortFile, 'utf8')).trim().split(/\r?\n/)[0];
        await jsonFetch(`http://127.0.0.1:${debugPort}/json/version`);
        break;
      } catch {
        if (i === 29) throw new Error('Chrome remote debugging did not become ready');
        await delay(250);
      }
    }
  }

  const proxyEnv = { ...process.env, CDP_PROXY_PORT: proxyPort };
  if (process.platform === 'win32') proxyEnv.LOCALAPPDATA = profile;
  else proxyEnv.HOME = profile;
  proxy = spawn(process.execPath, [path.join(webAccessDir, 'scripts', 'cdp-proxy.mjs'), '--browser', 'chrome'], {
    env: proxyEnv,
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  const base = `http://127.0.0.1:${proxyPort}`;
  for (let i = 0; i < 30; i++) {
    try { await jsonFetch(`${base}/health`); break; }
    catch { if (i === 29) throw new Error('CDP proxy did not become ready'); await delay(250); }
  }
  const created = await jsonFetch(`${base}/new`, { method: 'POST', body: 'https://example.com' });
  targetId = created.targetId;
  let info = {};
  let evaluated = {};
  for (let i = 0; i < 40; i++) {
    info = await jsonFetch(`${base}/info?target=${encodeURIComponent(targetId)}`);
    evaluated = await jsonFetch(`${base}/eval?target=${encodeURIComponent(targetId)}`, {
      method: 'POST', body: 'document.querySelector("h1")?.textContent'
    });
    if (info.url?.startsWith('https://example.com') && evaluated.value === 'Example Domain') break;
    await delay(250);
  }
  const ok = info.url.startsWith('https://example.com') && info.title === 'Example Domain' && evaluated.value === 'Example Domain';
  console.log(JSON.stringify({ ok, adapter: 'web-access', url: info.url, title: info.title, marker: evaluated.value }));
  process.exitCode = ok ? 0 : 1;
} catch (error) {
  console.error(JSON.stringify({ ok: false, adapter: 'web-access', error: error.message }));
  process.exitCode = 1;
} finally {
  if (targetId && proxy) {
    try { await jsonFetch(`http://127.0.0.1:${proxyPort}/close?target=${encodeURIComponent(targetId)}`); } catch {}
  }
  if (proxy) { proxy.kill('SIGTERM'); await delay(200); if (!proxy.killed) proxy.kill('SIGKILL'); }
  if (browser) { browser.kill('SIGTERM'); await delay(200); if (!browser.killed) browser.kill('SIGKILL'); }
  await rm(profile, { recursive: true, force: true });
}
