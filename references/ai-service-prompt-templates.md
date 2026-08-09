# Additional Web-AI Roles and Prompt Templates

Use this reference when the user selects DeepSeek, Doubao, Kimi, Qwen, or Zhipu Qingyan. Product features and model names change; verify the visible account, model, search/research mode, source behavior, and date before submission. These services generate leads, structures, translations, or critiques—not evidence by themselves.

## Contents

- [Selection guide](#selection-guide)
- [Shared prompt contract](#shared-prompt-contract)
- [DeepSeek](#deepseek)
- [Doubao](#doubao)
- [Kimi](#kimi)
- [Qwen](#qwen)
- [Zhipu Qingyan](#zhipu-qingyan)

## Selection guide

| Service identity | Prefer for | Do not rely on it for |
| --- | --- | --- |
| **DeepSeek** | Causal decomposition, hard trade-offs, contradiction audit, structured reasoning in Chinese or English | Current social facts or source claims unless live search and direct URLs are visibly enabled |
| **Doubao** | Chinese consumer language, Douyin/Chinese-platform framing, culturally native copy hypotheses, multimodal creative review | Broad prevalence claims or source traceability without opened originals |
| **Kimi** | Long-context evidence packets, Chinese source reading, source-linked synthesis, competitor discovery when a search-capable thinking mode is available | Treating model recall as current market evidence |
| **Qwen** | Bilingual classification, structured extraction, technical/product context, translation-risk checks, schema-first synthesis | Current platform performance without native originals |
| **Zhipu Qingyan** | Chinese market structure, institutional or policy-oriented synthesis, argument mapping, long-form red-team review | Regulatory or policy claims without authoritative verification |

Assign one bounded job per service. If two services would receive the same prompt, choose one unless the user explicitly requests a latency hedge. Always save the exact prompt and normalized conversation URL immediately after submission.

## Shared prompt contract

Every prompt must include:

```text
Role and why this service is selected:
Brand/account and official URLs:
Verified facts:
Working hypotheses:
Decision affected:
Audience, market, languages, and target platforms:
Time window:
Assigned branch and bounded questions:
Required original sources and visible metrics:
Output schema:
Evidence / inference / uncertainty labels:
Anti-fabrication and inaccessible-source rules:
Reversal condition:
Round objective:
```

Require original-language sources where translation changes meaning. When live search is unavailable, provide a source packet and restrict the service to synthesis or critique.

## DeepSeek

**Identity:** skeptical strategy analyst and causal decomposer.

```text
Act as a skeptical growth-strategy analyst for [BRAND/ACCOUNT and OFFICIAL URLS]. Your job is causal decomposition and contradiction, not broad market recall.

Decision: [DECISION].
Verified evidence packet: [SOURCE-LINKED FACTS, ORIGINAL POSTS, DATES, VISIBLE METRICS].
Audience/market/platforms: [DETAILS].
Constraints: [TEAM, ACCESS, BUDGET, CADENCE, BRAND/LEGAL LIMITS].

Test these beliefs: [BELIEFS]. For each, return the strongest support, strongest contradiction, alternative explanation, missing variable, reversal evidence, and cheapest discriminating experiment. Then rank [N] mechanisms by decision value and reject at least one attractive but weak option.

Use only the supplied evidence unless live search is visibly enabled. If using search, give direct original URLs and dates. Separate observation, inference, and decision. Do not invent metrics, quotes, prevalence, or current platform facts. Round objective: contradiction and experiment design.
```

## Doubao

**Identity:** Chinese social-language and culturally native creative analyst.

```text
作为[目标平台，如抖音/小红书/视频号]的中文用户语言与创意机制研究员，为[品牌/账号及官方链接]分析内容表达，不代替原始数据调研。

决策：[需要改变的内容或增长决策]。
目标人群/市场：[人群、地区、语言、使用场景]。
已核验素材：[原帖链接、日期、可见指标、评论原文或可靠转述]。
约束：[品牌边界、文化风险、拍摄资源、频次、审批要求]。

请输出：
1. 用户可能使用的原生搜索词、问题句式和情绪表达；
2. 每组表达对应的心理任务、焦虑和期望回报；
3. 可迁移的首帧、叙事、证明和互动机制；
4. 哪些表达在目标市场可能显得官话、夸张、冒犯或失真；
5. 三个最小可测试版本及停止条件。

必须区分原始证据、语言推断和创意建议。不要虚构热度、平台搜索量、用户共识或评论。若启用联网搜索，为每个关键判断提供可打开的原帖链接和日期。Round objective：本土语言与创意机制假设。
```

## Kimi

**Identity:** long-context evidence librarian and source-linked synthesis analyst.

When Perplexity visibly offers **Kimi K3 Thinking**, prefer it for competitor discovery when source traceability is adequate. Otherwise use the closest current Kimi search/thinking mode and record the actual selection.

```text
Act as a source-linked social-market research librarian for [BRAND/ACCOUNT and OFFICIAL URLS]. Read the supplied context and search only to fill the named evidence gap.

Decision: [DECISION].
Target buyers/users, markets, languages, and platforms: [DETAILS].
Known evidence: [SOURCE PACKET].
Missing branch: [DIRECT COMPETITORS / ANALOGOUS MECHANISMS / CHINESE USER LANGUAGE / OTHER].
Time window: [DATES].

Return [N] cases in a ledger with: account/brand; why it is direct or analogous; business model and audience overlap; direct profile URL; 2–3 original post URLs; date; first line/frame; visible labelled metrics; comment/search intent; mechanism; limitation; decision affected. Include at least one disconfirming or poor-performing case.

Do not infer competitor status from visual similarity. Do not use search snippets as hard evidence, reconstruct inaccessible posts, or invent engagement, saves, shares, reach, or conversion. Mark every item original-opened, authoritative, lead-only, or blocked. Round objective: bounded discovery and source ledger.
```

## Qwen

**Identity:** bilingual taxonomy, structured extraction, and translation-risk analyst.

```text
Act as a bilingual evidence-structuring analyst for [BRAND/ACCOUNT].

Decision: [DECISION].
Languages/markets/platforms: [DETAILS].
Evidence packet: [ORIGINAL-LANGUAGE POSTS, COMMENTS, CAPTIONS, URLs, DATES, METRICS].
Required schema: [FIELDS OR TABLE].

Normalize the packet into: source ID; original language; literal meaning; culturally natural paraphrase; audience job; anxiety/objection; search phrase; opening mechanism; proof; CTA; visible metric; source limitation; transfer risk; target-platform experiment. Preserve ambiguous wording and explain translation choices.

Do not smooth away disagreement, infer prevalence, or translate a culturally specific phrase into a universal claim. Use only supplied evidence unless current search is enabled and direct sources can be opened. Round objective: bilingual normalization and structured extraction.
```

## Zhipu Qingyan

**Identity:** Chinese market-structure and institutional red-team analyst.

```text
作为[行业/平台]的市场结构与反方审计研究员，对[品牌/账号及官方链接]的社媒增长假设进行压力测试。

决策：[决策]。
目标市场/人群/平台：[详情]。
已核验事实与来源：[资料包]。
关键假设：[假设]。
可能涉及的政策、文化或机构风险：[风险]。

请分别给出：市场角色与利益关系、支持证据、反例、替代解释、检索覆盖盲区、需要权威来源核验的事项、会推翻决策的最小证据，以及一个可逆实验。政策或法规只提供待核验线索，并列出应访问的官方机构或一手页面；不要把模型知识当成当前规则。

区分事实、机构/媒体主张、推断、未知和决策。禁止虚构政策、比例、案例、引用或共识。Round objective：市场结构与制度风险反方审计。
```
