# 8 月 1 日项目补漏检查

这轮没有改动两张 Infra 主图：Agent Infra 仍是 74 个项目，Model Infra 仍是 58 个。项目表从 257 条增到 261 条，新增的是观察池，不是主图 logo。

## 扫描结果

- 近期创建窗口：2026-05-01—2026-08-01。
- 重新读取旧候选池 222 条，并执行 12 组 GitHub 定向搜索。
- GitHub 搜索得到 295 条跨 query 命中；与旧候选池合并去重后复核 444 个候选。
- 应用“最近三个月新建、OpenRank 加速或关注度明显上升”的高召回条件后，保留 341 条待查记录。
- 主表 132 个入图项目中，125 个有 2026 年 7 月 OpenRank；全库 7 月分区仍在回填，因此只把它当方向信号。

## 新增到 CSV 观察池

| 项目 | 8 月 1 日口径 Stars | 5—7 月 OpenRank | 为什么要盯住 | 为什么暂不加主图 |
|---|---:|---|---|---|
| [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | 8,065 | 0 / 29.98 / 32.65 | meta-harness 同时覆盖编排、策略、sandbox 与协作 | Coding harnesses 和 framework 两区已满，先看外部采用 |
| [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | 5,971 | 12.26 / 27.50 / 19.27 | 新出现的开源 coding agent，连续三个月有协作信号 | Agentic coding 已有 12 个 logo，短期内不继续加密 |
| [xai-org/grok-build](https://github.com/xai-org/grok-build) | 24,003 | 0 / 0 / 0 | 7 月中旬发布后快速进入 GitHub Trending | 历史不足三周，OpenRank 尚无有效值，不能只凭热度入图 |
| [vercel/eve](https://github.com/vercel/eve) | 4,283 | 0 / 5.68 / 12.88 | markdown、sandbox 与 workflow 组合出的 agent framework | 与 Vercel AI SDK 和现有 framework 有谱系重叠 |

## 已在 CSV、继续不单列 logo

- `langchain-ai/deepagents`：7 月 OpenRank 159.30，但主图已有 LangChain；作为同一谱系的 harness 演化讲，不再重复 logo。
- `vllm-project/vllm-ascend`：7 月 OpenRank 48.15，是重要硬件适配，但它更适合作为 vLLM 的插件生态证据。
- `NVIDIA/OpenShell`：7 月 OpenRank 30.27，sandbox 区已有四个互补代表；继续观察其独立社区结构。
- `OpenHands/software-agent-sdk`：7 月 OpenRank 36.33，属于 OpenHands 拆分 SDK，放进项目详情而不是主图。
- `coze-dev/coze-loop`：7 月 OpenRank 30.54，Observability 区已有四个代表项目，暂不增加第五个相似平台。

## 结论

7 月数据没有暴露新的结构缺口，所以不需要为“更新”而改主图。真正需要修的是发现方法：除了绝对 Top-N，还要固定保留一条近三个月新生与加速项目通道。新项目先进入 CSV 观察池；只有当它补上结构空白，或足以替换同区现有项目时，才进入 landscape。
