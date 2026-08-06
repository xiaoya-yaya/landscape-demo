# ZenMux Token Economics｜两张补充洞察

页面来源：<https://arena.zenmux.ai/token-economics?view=value>

页面快照：2026-08-06 12:47 UTC。截图保留 ZenMux 页面原生的厂商聚焦状态，演讲页只增加高亮框、结论和出处。

## 图表口径

- 数据范围：ZenMux 平台内的模型 token 消耗，不代表全市场份额。
- 横轴：标准篮子价格，对应 100,000 个输入 token 和 1,000 个输出 token，使用官网每百万 token 价格计算。
- 纵轴：模型发布后前 14 个工作日内，各活跃日 token 量的中位数。
- 气泡大小：日 token 中位数除以标准篮子价格，页面称为 Value。
- 颜色：模型厂商。
- 象限：横、纵轴各自的样本中位数形成四个象限。
- 免费或没有价格的模型不进入 Value Map；发布不足 14 个工作日的模型带 `*`。

本次页面列出 142 个文本模型、20 家厂商；其中 127 个模型同时有使用量和有效价格，进入 Value Map。价格中位数约为 0.077 美元，发布期日 token 中位数约为 928 万。

## 视角一｜高价 + 高使用区

把模型限定到价格高于中位数、发布期日 token 也高于中位数的象限，再按日 token 中位数排序：前 10 个模型中有 7 个来自 Anthropic。

这组数据支持的说法是：在 ZenMux 的当前样本里，较高价格没有把 Anthropic 挤出需求中心。它不能单独解释选择原因，也不能据此判断全市场份额。能力、延迟、可用性和工作负载仍要另外验证。

截图：[`public/keynote/large-models/zenmux-premium-demand.png`](../../../public/keynote/large-models/zenmux-premium-demand.png)

## 视角二｜价值效率前沿

页面 Value 排名前三：

1. DeepSeek V4 Flash 0731：标准篮子 0.01428 美元，发布期日 token 中位数约 201.38 亿，观察窗口未满；
2. DeepSeek V4 Pro：标准篮子 0.04437 美元，发布期日 token 中位数约 77.15 亿；
3. Ling-3.0-flash：标准篮子 0.00618 美元，发布期日 token 中位数约 7.68 亿，观察窗口未满。

DeepSeek 占据前两名，InclusionAI 的 Ling-3.0-flash 排第三。两个带星号的新模型仍处于发布初期，这一页呈现的是当前信号，不作为长期排名。

截图：[`public/keynote/large-models/zenmux-value-frontier.png`](../../../public/keynote/large-models/zenmux-value-frontier.png)

## 演讲页上的出处

两页统一标注：

> 来源：ZenMux Arena · Token Economics｜ZenMux token 消耗数据 + 官网模型价格｜页面快照：2026-08-06

价格页：<https://zenmux.ai/models?sort=newest&supported_protocol=chat.completions>
