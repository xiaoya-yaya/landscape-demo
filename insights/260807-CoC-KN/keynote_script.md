# CommunityOverCode China 2026 Keynote 演讲执行稿

> 标题：Agentic AI 新趋势下，开放生态的那些老规矩
> 时间：2026 年 8 月 7 日
> 演讲：30 分钟，中文
> 研究页：<https://landscape.16507.cn/keynote>
> 舞台播放：<https://landscape.16507.cn/keynote/present>

这份文件保留舞台执行说明。当前播放模式共有 23 个场景；可直接照读的 30 分钟版本见 [`keynote_verbatim_30min.md`](./keynote_verbatim_30min.md)。屏幕里运行的是网页本身：生态图保留真实项目和布局，Apache 与 InclusionAI 保留原来的 Tab、项目卡和技术栈。翻页笔或触屏手势替演讲者完成切换和聚焦。

## 这场演讲怎样走

前半段先让观众看见变化：协议成为独立层，推理系统继续拆分，开放权重进入主流使用，README 开始带有执行语义。

接着把视线往系统底部移。Agent 进入生产环境以后，会直接碰到状态、调度和失败恢复。Apache 长期维护的正是这类问题。

InclusionAI 把“谁可以参与”展开到模型、具身智能、基础设施和真实服务。模型时代的开放对象也因此变多了。许可证依然重要，权重之外的材料需要单独说明。

结尾回到 CommunityOverCode。公开入口、公开过程和随贡献积累的信任，仍然是让陌生人能够一起维护技术的办法。

## 翻页笔

舞台模式只有一条前后轴。“下一页”和“页内下一步”是同一个动作，进入和退出全屏单独控制。

| 操作 | 结果 |
|---|---|
| `PageDown`、`↓`、`→` | 下一步：切换 Tab、聚焦区域、操作生态图或进入下一场景 |
| `PageUp`、`↑`、`←` | 上一步：严格按原路径退回，页内状态也会恢复 |
| `Enter` | 进入全屏，不改变当前画面 |
| `Esc` | 退出全屏，不离开舞台播放页 |

翻页笔继续使用 `PageDown` / `PageUp`。MacBook 上可以直接用四个方向键排练。正式演讲时不需要鼠标，也不需要点击网页里的 Tab、项目卡或生态图。

## 上台前

1. 打开 <https://landscape.16507.cn/keynote/present>。Large Models、两张 ZenMux 洞察和 Awesome 使用预先生成的画面，翻页不依赖现场网络。
2. 按 `Enter` 进入全屏，确认画面没有变化；按 `Esc` 退出，再按 `Enter` 回到全屏。
3. 按一次“下一步”，确认粉色 Agent Infra 和蓝色 Model Infra 两张旧版静态图完整出现；再按一次“上一步”回到标题。
4. 前进到新版 Agent Infra，确认整张动态生态图已经出现；连续检查三次“下一步”：`Agentic coding`、`Personal AI assistants`、`Memory, knowledge & context` 应依次聚焦。
5. 继续检查 Model Infra：`Model API gateways`、`Serving · Inference`、许可证视角应依次出现，最后一次恢复全图。
6. 继续检查 Large Models：第一屏应完整显示六个领域；随后依次切到 Top 10、开放权重、AAI 可比样本，卡片数量应为 10、24、10。
7. Large Models 之后应连续出现两张 ZenMux 图：第一张聚焦 Anthropic，第二张聚焦 DeepSeek 与 InclusionAI。确认高亮框没有压住模型名称。
8. 继续检查 Awesome：随后依次切到可直接消费项目、安装类项目、全量视角。安装类项目的卡片会解释 `Install` 与 `direct` 的口径。
9. 用“上一步”原路退回标题。正式演讲前不要刷新页面。
10. 若浏览器拦截全屏，先在浏览器设置中允许当前站点使用全屏。

数据口径：

- 全场统计口径：数据截至 2026-08-01。
- OpenRank：趋势字段覆盖 2025-08—2026-07，舞台分析使用 2026-07 完整月；7 月全库分区仍在回填，因此只把它当方向信号。
- OpenRouter 与 ZenMux：2026-07-01—2026-07-31 完整自然月。
- ZenMux Token Economics 两张补充图：页面快照生成于 2026-08-06；使用 ZenMux 平台 token 消耗数据和官网模型价格。
- GitHub 仓库指标：采用当前 REST API 返回值，按演讲约定归入 8 月 1 日快照。

---

## 01｜标题（0:00—0:35）

### 画面

标题页。屏幕下方只保留很轻的播放提示。

### 讲法

大家好。今天这个题目里有两个时间尺度。

Agentic AI 的变化很快，新模型、新框架和新协议不断出现。开放生态的很多问题却很旧：别人能不能找到入口，能不能理解一项技术为什么这样做，能不能在原作者离开以后继续维护。

我想用半个小时，把这两件事放在一起看。

### 翻页笔

按 `PageDown`，进入现场调查页。

---

## 02｜现场有多少人见过这两张图（0:35—1:05）

### 进入画面

粉色 Agent Infra 与蓝色 Model Infra 两张旧版静态图并排放置。屏幕上只问一句：

> 现场有多少人见过这两张图？

### 讲法

在正式开始之前，我先问一下：现场有多少人见过这两张图？见过其中任何一张，都可以举一下手。

停几秒，看现场。然后说：

这是我们此前发布的 Agent Infra 和 Model Infra Landscape。今天再把它们拿出来，是因为这两张图一直在变，我们也一直在重新检查里面的项目和分类。

按 `PageDown`，进入问题页。

---

## 03｜图一直在变，什么值得留下（1:05—1:50）

### 进入画面

左侧只有一句事实：Agentic AI 的项目名单，几个月就要重画一次。

### 讲法

我们维护 Agentic AI Landscape 的感受很直接：项目名单几个月就要重新检查。很多仓库突然出现，也有一些项目改名、合并，或者不再适合占据主图的位置。

更新生态图时，star 榜单只是发现候选的信号。我们真正要判断的是，一项技术有没有形成别人可以接手的公共能力。

### 按一次 `PageDown`

右侧出现：

> 开放生态真正关心的是：别人能不能接住它，继续往下做。

### 继续讲

接下来四张图，是从四个角度看同一个生态。每张图会切几次视角，所有观点都落到图上的项目、分区或筛选结果。

再按 `PageDown`，进入 Agent Infra。

---

## 04｜Agent Infra：入口很热，变化发生在更下面（1:50—3:25）

### 进入画面

Agent Infra 的真实网页组件铺满屏幕，项目 Logo、分区和 OpenRank 权重都保留。先让观众看 3—5 秒，不要急着翻页。

### 讲法

这张图沿着 Agent 完成一次任务的路径来组织项目。上面有应用和框架，下面是工具、环境、记忆、协议和运行基础设施。

这张图有 74 个项目。先看当前结构，再看社区热度落在哪里，以及它带动了哪些基础设施需求。

### 按一次 `PageDown`

`Agentic coding` 自动抬高并高亮；右下角出现：

> 22 / 74：最大的两个 section 都围绕 coding

### 继续讲

Agentic coding 有 12 个项目，Code-first frameworks 有 10 个。代码仍是 Agent 生态最密集的入口，也是新项目最容易获得用户反馈的地方。

### 再按一次 `PageDown`

`Personal AI assistants` 抬高；讲解卡切换为：

> TOP 2：7 月 OpenRank 前两名都是 Personal AI assistants

### 继续讲

74 个项目里，7 月 OpenRank 排名前两位的是 OpenClaw 和 Hermes Agent，分别为 462.71 和 350.21。Personal AI assistants 这一栏共有 7 个项目，其中 5 个是在 2025 年 7 月以后出现的。

代码仍是项目最密集的入口，社区热度已经明显落到长期运行的个人 Agent 上。它们需要记住用户、复用 skills，也要持续连接外部服务。

### 再按一次 `PageDown`

`Memory, knowledge & context` 抬高；讲解卡显示：

> OpenViking · OpenRank：112.46 → 177.61

### 继续讲

OpenViking 把 memory、RAG 和 skills 收进 context database。2026 年 3 月到 7 月，它的 OpenRank 从 112.46 升到 177.61。

个人 Agent 开始长期运行以后，上下文不能一直塞在 prompt 或某个 framework 内部。存储、检索和更新需要单独管理，这也解释了 context database 为什么会在这一轮出现。图上的 `RISING` 只给有时间窗口证据的项目；它和“这一版刚加入主图”是两个字段。

再按 `PageDown`，进入 Model Infra。

---

## 05｜Model Infra：Gateway 又热了，但职责已经分叉（3:25—5:05）

### 进入画面

Model Infra 的真实网页组件铺满屏幕。第一眼只看全图，不显示观点卡。

### 讲法

Model Infra 看的是模型访问、训练、数据、计算和推理。现在有 58 个项目，其中 6 个在 Model API gateways。

### 按一次 `PageDown`

Model API gateways 自动聚焦，项目 Logo 和分区仍然可见；右下角出现：

> OmniRoute · OpenRank：4.48 → 31.92

### 继续讲

OmniRoute 在 8 月 1 日口径下有 38,536 stars，2 月到 7 月 OpenRank 从 4.48 升到 31.92。机器扫描发现了它，按绝对排名截断的人工短名单却把它漏掉了。

这次把它补回来，也补了一条高增速复核通道。增长只能说明值得重看，不能替代功能判断。

我们又对照了几个 gateway 的近期实现。它们都开始进入 Agent 的调用链，站的位置却不一样。

LiteLLM 位于 Agent 和上游 MCP Server 之间。它接管 OAuth，取得 `tools/list`，代理 `tools/call`，也能按用户限制可调用的工具。这里管理的是 Agent 对外部工具的访问。

AgentGateway 是协议感知的数据平面。MCP、A2A 和 LLM 请求进入以后，它先识别协议，再执行路由和流量策略。1.1 把 MCP JWT 鉴权移到 route level，身份信息可以继续用于工具授权、限流和请求转换。它代理的是协议流量，不是把自己包装成一个 Agent。

ContextForge 更接近注册中心和聚合代理。它把多个 MCP Server、A2A Agent 以及 REST、gRPC 服务登记在一个目录里，组合成统一入口；还可以把外部 A2A Agent 暴露成 MCP Tool。这样，只懂 MCP 的客户端也能调用那个 Agent。它曾加入 Rust A2A runtime，但这套 Rust sidecar 已被官方弃用，现场不要再把 runtime 当作当前趋势来讲。

OmniRoute 的方向又不同。它把自己的模型路由、额度、成本和健康状态做成 MCP 工具，同时把自己包装成带有 `smart-routing` 等固定技能的 A2A Agent。Agent 可以把“替我选一个合适的模型并执行请求”委托给它。它不是通用的 MCP Server 或 A2A Agent 聚合代理。

这一页真正要讲的趋势是：Gateway 开始接管工具与 Agent 调用链。同叫 gateway，有的代理工具访问，有的执行流量策略，有的聚合协议后端，还有的把自身能力直接开放给 Agent。分类时要看它在链路中的位置和实际动作，不能只看项目介绍里有没有 MCP、A2A 两个词。

证据来自各项目官方仓库与 release：

- LiteLLM releases：<https://github.com/BerriAI/litellm/releases>
- AgentGateway 1.1 release notes：<https://agentgateway.dev/docs/kubernetes/1.1.x/reference/release-notes/>
- AgentGateway MCP authorization：<https://agentgateway.dev/docs/standalone/latest/mcp/mcp-authz/>
- ContextForge architecture：<https://ibm.github.io/mcp-context-forge/latest/architecture/>
- ContextForge A2A integration：<https://ibm.github.io/mcp-context-forge/using/agents/a2a/>
- OmniRoute MCP Server：<https://github.com/diegosouzapw/OmniRoute/blob/main/docs/frameworks/MCP-SERVER.md>
- OmniRoute A2A Server：<https://github.com/diegosouzapw/OmniRoute/blob/main/docs/frameworks/A2A-SERVER.md>

### 再按一次 `PageDown`

`Serving · Inference` 自动聚焦；讲解卡显示：

> 6 → 8：Serving · Inference

### 继续讲

推理区增加的并不都是 engine。LMCache 处理 KV cache 复用，vLLM-Omni 处理多模态 serving。Agent 请求更长、重复前缀更多，cache、调度与恢复开始单独形成项目。

### 再按一次 `PageDown`

全图恢复，右下角显示：

> 39 / 58：Model Infra 中三分之二采用 Apache-2.0

### 继续讲

Model Infra 经常涉及硬件适配、专利授权和多家公司共同维护。Apache-2.0 在这一层明显多于其他许可证，后面的 Apache 与许可证章节会回到这个问题。

OpenRank 在这里表示协作活跃度，不表示性能排名。

再按 `PageDown`，进入 Large Models。

---

## 06｜Large Models：开放权重进入主流使用区（5:05—6:15）

### 进入画面

Large Models 总览铺满舞台。六个领域、筛选栏和每张模型卡都应完整出现。

### 讲法

这张图换了一个数据来源。GitHub 活跃度不适合说明模型的实际使用，因此我们把 OpenRouter 和 ZenMux 放在同一个完整自然月里比较。

选择集一共 50 个模型 endpoint，其中 20 个提供公开权重，30 个没有公开权重。开放权重仍占重要位置，但没有占据多数。

### 按一次 `PageDown`

画面切到 `TOP 10`，50 张模型卡收束到真实使用前十；右下角同时出现：

> Top 10：开放权重 4 / 无公开权重 6

### 继续讲

开放权重模型已经进入主流使用区。这个结果不等于开放模型已经赢了，也不能代表整个模型市场。它说明社区可获得的模型，已经能够和闭源 API 出现在同一个真实使用区间里。

### 再按一次 `PageDown`

画面切到开放权重视角；右下角显示：

> Reasoning：9 / 10 为开放权重

### 继续讲

开放程度和模型类型有关。Reasoning 区几乎都是开放权重模型；Multimodal / VLM 则相反，30 个模型中有 22 个没有公开权重。这两类能力走出了不同的发布路径。

### 再按一次 `PageDown`

画面切到 AAI 可比样本；右下角显示：

> 使用 #1 / AAI 第一模型使用 #23

### 继续讲

这一屏保留了匹配样本中的 AAI 前 10。GLM 5.2 在使用榜排第 1，AAI 是 51.1；Claude Opus 5 的 AAI 最高，为 60.7，使用排名却是第 23。部署成本、价格和渠道都会改变实际选择。

再按 `PageDown`，进入 ZenMux 的价格与使用视角。

---

## 07｜ZenMux：高价区仍有清晰的需求中心（6:15—6:40）

### 进入画面

ZenMux Token Economics 的 Value Map 铺在左侧，原生筛选聚焦 Anthropic。橙色框圈住右上方模型集群。

### 讲法

ZenMux 把标准篮子价格和平台内真实 token 使用放在一张图上。右上角是价格高于中位数、发布期日 token 也高于中位数的模型。

这个象限按日 token 中位数排序，前十里有七个来自 Anthropic。高价格没有把这些模型挤出 ZenMux 的需求中心。图表本身不能解释原因，能力、延迟和工作负载仍要另外验证。

按 `PageDown`，进入价值效率视角。

---

## 08｜ZenMux：价值效率前沿里的 DeepSeek 与 Ling（6:40—7:05）

### 进入画面

同一张 Value Map 改为聚焦 DeepSeek 与 InclusionAI。绿色框圈住 DeepSeek V4 Flash、DeepSeek V4 Pro 和 Ling-3.0-flash。

### 讲法

价格低于中位数、使用高于中位数的区域里，DeepSeek V4 Flash 和 V4 Pro 排在 Value 指标前两位，Ling-3.0-flash 排第三。

Value 用发布后前 14 个工作日的活跃日 token 中位数除以标准篮子价格。Flash 和 Ling 的观察窗口还不完整，现场要说成发布初期信号。数据只代表 ZenMux 平台，不代表全市场份额。

按 `PageDown`，进入 Awesome。

---

## 09｜Awesome：README 开始带有执行语义（7:05—8:25）

### 进入画面

Awesome Agentic Landscape 总览铺满屏幕，保留四列、筛选栏和项目卡。

### 讲法

前三张图主要看代码项目。这张图看另一种开源资产：instructions、skills、prompts、templates 和工作流。

它们不一定运行一个服务，也可能没有复杂代码。它们把人做过一件事的顺序和约束保存下来，让 Agent 可以直接使用。

### 按一次 `PageDown`

画面打开 `AGENT-READY`，只保留可以被 Agent 直接消费的项目；右下角出现：

> 入图的 26 个项目中，19 个可被 Agent 直接消费

### 继续讲

README 过去主要解释软件怎么安装。现在有些 README 已经在告诉 Agent 应该按什么顺序做事、什么条件不能越过、结果应该怎样检查。

这是一种很轻的接口。经验正在成为可复用的开源资产。

### 再按一次 `PageDown`

画面聚焦 `Install`；右下角显示：

> 7 / 7：7 个安装类项目都给出了机器可执行入口

### 继续讲

这里的 `Install` 是编辑分类，指安装或注册工具；`direct` 是材料形态，表示仓库提供 Agent 可直接调用的命令、manifest 或配置。这 7 个项目都满足该条件。它衡量入口是否能执行，不评价项目质量或成熟度。

### 再按一次 `PageDown`

画面恢复全图；右下角显示：

> 22 / 26：创建于 2025 年以后

### 继续讲

这是编辑样本的年龄结构，不能外推到 GitHub 全量。它说明这些 Agent-native 知识资产形成得很快，项目之间的格式和分发方式还会继续变化。

再按 `PageDown`，进入筛选方法。

---

## 10｜四张图怎样形成这次观察（8:25—9:45）

### 进入画面

屏幕列出四张图各自的数据源、时间窗与最终样本：

- Agent Infra：OpenDigger 与 GitHub，74 个入图项目；
- Model Infra：共用仓库候选池，58 个入图项目；
- Large Models：OpenRouter、ZenMux 与 Hugging Face，2026 年 7 月完整自然月，50 个模型 endpoint；
- Awesome：GitHub、OpenDigger 与手工种子，26 个编辑样本。

### 讲法

四张图没有共用一个排行榜。研究对象不同，取样单位也不同。Agent Infra 和 Model Infra 看 GitHub 仓库与协作信号；Large Models 看完整月份的实际使用，再由 Hugging Face 核验官方权重；Awesome 还要阅读 README，确认内容能否被 Agent 直接使用。

### 第一次按 `PageDown`

四行分别展开筛选与复核路径。

### 继续讲

基础设施项目会检查仓库状态、README 和它在技术结构里的位置。绝对 Top-N 之外，还会单独复核最近 90 天新建项目，以及 OpenRank、WatchEvent 的加速信号。模型 endpoint 先在各平台内部计算分位，避免把两家的 token 数直接相加。Awesome 的判断落在仓库材料上：有没有可安装的 skill、instruction、hook 或 workflow。

### 第二次按 `PageDown`

下方出现四项共同判断：完整时间窗、数据粒度、证据相互校验、编辑取舍。

### 继续讲

每张图都要标清时间窗。仓库、模型 endpoint 和知识资产分开统计。使用量、协作活跃与发布材料各自回答不同问题，不能互相代替。进入主图还会检查结构缺口和重复表达。

### 第三次按 `PageDown`

底部出现 `OBSERVATION / CONCLUSION / INITIATIVE`。

### 继续讲

这轮观察里，开放权重已经进入主流使用；协议、推理和可执行知识资产也在增厚。

采用数据告诉我们有没有人在用。许可证与发布材料决定社区拿到以后能做什么，还缺什么。

接下来我们会把每次更新的快照、脚本和入图理由一起发布。项目社区可以在仓库里补充证据或提出修正，让下一版建立在可复核的材料上。

再按 `PageDown`，进入 Apache 转场。

---

## 11｜Agent 跑起来以后，工程和开放开始变得具体（9:45—10:20）

### 进入画面

深色背景，只显示标题。

### 讲法

四张图看完以后，我想把视线往下移。

Agent 进入真实系统，会遇到软件工程里很熟悉的问题。

### 按一次 `PageDown`

出现执行路径：

> 任务 → 共享状态 → 执行 → 失败怎么办？

### 继续讲

任务怎样编排，状态怎样在不同语言和系统之间传递，执行产生副作用以后怎样补偿。Apache 长期维护的正是这些系统问题。

再按 `PageDown`。

---

## 12｜Apache 的规模是一套长期协作能力（10:20—11:45）

### 进入画面

先出现：

> 290+ Open Source Projects

### 讲法

Apache 官网目前写的是 290 多个开源项目。这个数字背后还有一套发布和身份体系。

### 按一次 `PageDown`

其余三个数字出现：

- 1,300+ software releases
- 10,000+ committers
- 1,190+ members

### 继续讲

这些数字的口径不同。项目、年度发布、committer 和 member 不能相加，也不能与 GitHub 仓库数互换。

把它们放在一起，可以看到 Apache 的规模怎样形成：项目持续发布，贡献者逐步取得治理责任，仓库背后有一套长期运转的社区。

再按 `PageDown`，进入技术位置。

---

## 13｜Apache 在 Agent 的数据与运行底座（11:45—14:00）

### 进入画面｜Data, analytics & AI

上半部分保留 Apache 项目的 7 个技术领域，右侧停在 Data, analytics & AI。这套领域和数量来自 Apache Projects Directory 的项目分类，用来观察 Apache 全部项目的技术分布。同一项目可以出现在多个领域，数量不能直接相加。

画面下方始终列出进入 Agentic Landscape 的 6 个 Apache 项目，并按它们在 Agentic AI 技术栈里的实际角色分成两组。

### 讲法

如果只看 Agent UI 和框架，Apache 离热点有些远。数据、计算和运行系统里，它的位置很清楚。Apache Projects Directory 允许一个项目带多个分类，因此左侧领域数量会有重叠；页面直接写成“同一项目可属于多个领域”，台上不使用缩写。

Apache Projects Directory 的标签是统计来源，不适合直接拿来解释这六个项目。比如 Hudi 会落到 library，Paimon 和 Gravitino 又缺少可用领域标签。这里把两个口径分开，避免观众误以为六个项目都属于当前选中的 Data tab。

### 连续按 `PageDown`

右侧依次切换其余六个领域：Libraries、Network、Web、Cloud & Operations、Security、IoT & Geospatial。每一页都显示该领域的数量、范围和六个头部项目。现场快速扫过项目名，不需要逐个报 GitHub stars。

Libraries 可以点 ECharts、Arrow 和 Thrift；Network 可以点 Arrow、Thrift 和 Camel；Web 可以点 Tomcat 和 CouchDB；Cloud & Operations 可以点 SkyWalking、JMeter 和 Maven；Security 的项目很少，Ranger 排在最前；IoT & Geospatial 可以点 IoTDB 和 PLC4X。

画面下方始终保留 6 个 Landscape 入选项目。Airflow 和 Spark 放在“任务与计算”：一个组织任务，一个完成分布式计算。Iceberg、Hudi、Paimon 和 Gravitino 放在“Lakehouse 与元数据”。前三个处理开放数据表、增量更新和流批数据，Gravitino 负责跨系统的元数据与目录。

这个分布很集中。Apache 在当前 Agentic Landscape 里的六个项目，主要构成数据和计算底座。Agent framework、协议和应用层没有为了凑数硬放 Apache 项目。下一页会继续沿着实际运行链，看这些基础项目怎样接在一起。

再按 `PageDown`。

---

## 14｜蚂蚁深度参与的四个 Apache 项目（14:00—15:50）

### 进入画面

页面先展示完整运行链：Landscape 中的 6 个 Apache 项目，与蚂蚁深度参与的 4 个项目并排出现。三段技术角色都可见。

### 讲法

这里单独看四个蚂蚁深度参与的 Apache 项目。它们不需要被重新包装成 Agent 项目，直接看它们在运行链上解决什么。

### 第一次按 `PageDown`

第一段运行链被聚焦：Airflow 组织任务，Spark 完成大规模计算，Celeborn 让 shuffle 与 spilled data 稳定流动。

### 第二次按 `PageDown`

第二段被聚焦：Iceberg、Hudi、Paimon 和 Gravitino 维护开放的数据与元数据平面；Fory 处理高性能、多语言序列化和状态交换。

### 第三次按 `PageDown`

第三段被聚焦：GeaFlow 用流图计算维护持续变化的关系；Seata 处理跨服务事务、补偿和一致性。Agent 能够调用多个系统以后，“执行了一半”会成为真实的生产问题。

### 收束

四个项目落在同一条运行链上：数据移动、状态交换、关系上下文和失败恢复。

再按 `PageDown`，进入 InclusionAI。

---

## 15｜InclusionAI：AI Built By Everyone, For Everyone（15:50—17:20）

### 进入画面

复用研究页里的 InclusionAI Logo、理念和价值主张。平台数据此时还没有出现。

### 讲法

Apache 展示的是跨组织基础设施怎样长期协作。InclusionAI 提供了一个更靠近模型和 Agent 的样本。

这里的 “Everyone” 指很多种参与方式。Available 是模型和工具能被拿到、理解和适配；Affordable 是使用成本足够低，能够进入真实服务；Inclusive 是开发者、领域专家和普通用户都能参与，也能分享技术带来的价值。

### 按一次 `PageDown`

研究页原有的三张平台卡一起出现：

- GitHub：93 个公开仓库；
- Hugging Face：198 个公开模型；
- ModelScope：188 个公开模型。

### 继续讲

这三个数字不能相加。模型会跨平台发布，GitHub 与模型 Hub 的用户动作也不同。

它们共同说明的是，这套生态同时在发布软件和模型，并且覆盖三个组织：InclusionAI、AQ-MedAI 和 Robbyant。

再按 `PageDown`，进入技术栈。

---

## 16｜InclusionAI 的参与路径（17:20—20:20）

这一场景有五个状态。左侧是真实的技术栈 Tab，右侧保留项目 Logo、地址、角色和说明。每按一次 `PageDown`，active Tab 与右侧项目卡一起切换。

### 进入画面｜模型

Ling、Ring、LLaDA 和 Ming 分别关注语言、推理、扩散与全模态。开放材料里除了权重，还有模型卡、推理实现和阶段性 checkpoint。

### 第一次按 `PageDown`｜具身

Robbyant 的 LingBot 系列把地图、深度、世界模型和动作模型接起来。

这里的贡献入口很具体：空间数据、仿真环境、机器人适配和真实世界评测。

### 第二次按 `PageDown`｜Infra

这一层多停一会儿。

AReaL、AReno 处理训练与对齐；AWorld、AEnvironment 把任务、工具和环境组织成 Agent runtime；dInfer 让扩散语言模型能够高效运行。

没有大规模训练资源的开发者，也可以从环境接口、任务集、推理优化和可靠性进入。

### 第三次按 `PageDown`｜行业应用

医疗、UI 操作和搜索任务会提出不同的数据与评测要求。真实场景会改变下面每一层需要交付的材料。

### 第四次按 `PageDown`｜AI Service

LingGuang、金融服务和 AQ 等真实服务，把用户遇到的问题重新带回模型、环境和评测。

### 收束

这套图最值得讲的是许多具体的进入方式。

再按 `PageDown`，进入许可证问题。

---

## 17｜允许商用，够不够称为开放（20:20—21:05）

### 进入画面

屏幕只显示：

> 一个模型允许商用。够不够称为开放？

### 讲法

先留几秒给观众。

一份许可证可以允许使用、修改和分发。拿到模型以后，研究者仍然可能不知道它怎样训练，也无法复现实验。

### 按一次 `PageDown`

出现三个缺口：

> 训练代码？数据说明？评测方法？

### 继续讲

模型把开放对象扩展到了权重、数据和评测。许可证没有失效，它只负责其中一个问题。

再按 `PageDown`。

---

## 18｜三组许可证样本（21:05—22:35）

### 进入画面｜Agent Infra + Model Infra

132 个软件项目中，Apache-2.0 有 61 个，MIT 有 37 个，两者合计 74.2%。25 个 NOASSERTION 只表示 GitHub / SPDX 没有给出可确认的标识，不能直接读成没有许可证。

### 按一次 `PageDown`｜加入 Hugging Face Top 100

Hugging Face Text Generation 下载量 Top 100 中，Apache-2.0 有 57 个，MIT 有 19 个，两者合计 76%。Llama 3 系列的三种 tag 合计 8 个，Gemma 2 个，Apple AMLR 和 BLOOM RAIL 各 1 个；8 个标成 `other`，4 个没有 license tag。

`other` 和未标注都需要回到模型卡复核。Top 100 的单位是仓库，同一模型家族可能重复出现，也会混入量化、微调和测试仓库。

### 再按一次 `PageDown`｜加入调用量 Top 50 中的开放权重模型

2026 年 7 月的 OpenRouter 与 ZenMux 调用量 composite Top 50 中，有 20 个模型解析到官方公开权重仓库。MIT 有 8 个，Apache-2.0 有 6 个，合计 70%。调用量综合排名前三的 GLM 5.2、DeepSeek V4 Pro 和 DeepSeek V4 Flash 全部使用 MIT。

另外 6 个使用 Modified MIT 或模型专用条款：Kimi K2.7 Code、Kimi K2.6、Kimi K3、MiniMax M3、HY3 preview 和 Nemotron 3 Super。现场可以点出 Kimi K3 和 MiniMax M3：权重能够下载，商业使用和品牌要求仍要看各自条款。

调用量 Top 50 更接近头部模型，HF Top 100 提供一个更宽的仓库样本。两组都显示软件许可证仍然常见；模型专用或修改版条款在调用量头部里占 30%。

再按 `PageDown`，进入两份许可证的分发对照。

---

## 19｜Apache-2.0 与 OpenMDW-1.1 怎样约束分发（22:35—24:10）

### 进入画面

屏幕保留两条尚未展开的分发路径。

### 第一次按 `PageDown`｜Apache-2.0

Apache-2.0 允许分发 Source、Object 和 Derivative Works，不要求二进制分发时同时交出源码。

下游需要附许可证，显著标记修改过的文件，保留适用的原始声明；原作品带有 NOTICE 时，还要传递其中适用的内容。因相关 Work 或 Contribution 发起专利诉讼时，终止的是专利许可。条款没有处理模型推理输出。

### 第二次按 `PageDown`｜OpenMDW-1.1

OpenMDW 把模型架构、参数，以及实际置于该许可下的数据、代码和文档合称 Model Materials。它明示覆盖版权、专利、数据库权利和商业秘密权利。

下游分发时附许可证，并保留适用的版权和来源声明；没有修改文件标记和 NOTICE 机制。针对 Model Materials 发起专利或版权侵权诉讼时，全部授权终止，防御性应诉除外。生成输出不承接 OpenMDW 的使用、修改或分享义务。

两份许可证都允许商业使用，也都没有 share-alike。它们不会要求发布者补齐没有交付的训练代码和数据。

来源：

- Apache License 2.0：<https://www.apache.org/licenses/LICENSE-2.0.html>
- OpenMDW 1.1：<https://openmdw.ai/license/1-1/>
- OpenMDW FAQ：<https://openmdw.ai/faq/>

再按 `PageDown`。

---

## 20｜许可证给权利，材料决定研究能走多远（24:10—25:30）

### 第一次按 `PageDown`｜Rights

Apache-2.0 和 OpenMDW 都允许使用、修改和分发，具体分发手续、诉讼终止和输出边界不同。

OpenMDW 没有定义一套“衍生模型”分类。微调 checkpoint、adapter 和蒸馏模型怎样适用条款，要看下游实际分发了哪些 Model Materials。它明确写清的是生成输出：输出不承接 OpenMDW 的义务。

### 第二次按 `PageDown`｜Materials

许可证不会要求发布者自动补齐训练代码和数据。Model Openness Framework 检查发布材料，OSAID 给出 Use、Study、Modify、Share 所需的自由和 preferred form。

再按 `PageDown`，进入发布检查。

---

## 21｜一个模型发布，到底交付了什么（25:30—27:00）

### 进入画面

模型权重已勾选，状态显示：

> 只有权重，可下载

### 讲法

这页把“开放度”变成一个简单的发布检查。

权重能下载，至少说明模型可以运行。研究者还不知道结构与训练过程。

### 第一次按 `PageDown`

架构说明被勾选，状态变为：

> 结构清楚，可理解

### 第二次按 `PageDown`

训练代码与数据来源被勾选，状态变为：

> 训练材料较完整，可研究

### 第三次按 `PageDown`

评测方法和修改文档被勾选，状态变为：

> 评测与文档齐备，可继续修改

### 收束

现实里当然不会这么整齐，不同模型也有不同风险。这组检查只说明一个朴素事实：许可证无法替发布者补齐没有提供的材料。

再按 `PageDown`，进入社区。

---

## 22｜陌生贡献怎样变成长期信任（27:00—29:20）

这一页有五个状态。贡献路径沿用研究页的交互组件，`PageDown` 会移动 active 节点并替换下方说明。

### 进入画面｜发现入口

一个陌生贡献者首先需要知道项目现在缺什么。软件项目会提供 issue 和文档任务；模型项目还可以公开模型卡、数据说明和评测任务。

### 第一次按 `PageDown`｜提出变更

贡献者把问题和方案写在社区看得见的地方。大家围绕同一份上下文讨论。

### 第二次按 `PageDown`｜公开审查

Review 会找错，也会给技术选择、异议和取舍留下记录，让后来者理解为什么这样做。

### 第三次按 `PageDown`｜共同交付

代码、模型、文档和评测一起进入发布。发布把一次贡献变成社区需要长期承担的承诺。

### 第四次按 `PageDown`｜积累信任

Committer 和 member 的权限来自持续、可见、能被社区检验的工作。雇主和头衔不会自动带来治理权。

### 收束

CommunityOverCode 描述的就是这套机制：把陌生贡献逐步变成共同维护和治理责任。

再按 `PageDown`，进入结尾。

---

## 23｜结尾（29:20—30:00）

### 画面

> 老规矩继续有效。
> 现在，它们要覆盖模型、数据和评测。

下方是三个具体结果：

- 入口能被找到；
- 过程经得起回看；
- 信任跟着贡献增长。

### 完整口播

回头看今天的四张生态图，项目和分类还会继续变化。协议可能合并，推理系统会继续拆分，新的模型路线也会出现。

Agent 进入生产环境以后，调度、状态和失败恢复仍然需要长期维护。Apache 的项目和治理经验在这里重新显得重要。

InclusionAI 这样的技术栈把参与入口扩展到了模型、具身智能、基础设施和真实服务。许可证帮助我们说清权利；模型发布还要把研究和修改需要的材料交代清楚。

开放生态的老规矩继续有效：入口能被找到，过程经得起回看，信任跟着贡献增长。现在，这套机制需要覆盖代码以外的模型、数据和评测。

这也是我对 Community >>> Code 的理解。

谢谢大家。

说完停顿，再退出全屏。

## 时间不足时

- 四张生态图各保留一条结论，不展开项目。
- 方法页保留四套数据来源、共同判断准则和公开研究的后续动作。
- Apache 保留运行链；四个蚂蚁参与项目各用一个短语带过。
- InclusionAI 保留 Infra 与“许多进入方式”。
- 许可证保留 Rights / Materials 两层和发布检查的最后状态。
- 社区贡献路径至少讲“公开审查”和“信任跟随贡献”。

不要删除结尾。整场演讲需要在 Community >>> Code 上闭合。
