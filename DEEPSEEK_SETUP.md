# DeepSeek 配置与导师行为

## Streamlit Secrets

应用入口为 frontend/app.py。将以下内容填入 Streamlit 应用的 Secrets，填入自己的密钥：

```toml
API_BASE_URL = "https://k2cr2o7-api-om9i.onrender.com"
LLM_API_KEY = "YOUR-DEEPSEEK-API-KEY"
LLM_BASE_URL = "https://api.deepseek.com"
LLM_MODEL = "deepseek-v4-flash"
```

URL 使用纯文本，代码也兼容粘贴的 Markdown 链接外壳。密钥不要提交到 Git。本地从仓库根目录运行时，使用 .streamlit/secrets.toml；从 frontend 目录运行则使用 frontend/.streamlit/secrets.toml。

Streamlit 配有 LLM_API_KEY 时，在服务端直接请求 DeepSeek；没有配置时调用预测后端 /chat。独立后端需单独设置 LLM_API_KEY、LLM_BASE_URL、LLM_MODEL 环境变量。Secrets 不会自动同步到 Render。预测服务地址以用户确认的 -om9i 地址为准；旧 README 的不带后缀地址不能作为本部署依据。

## 两套 harness

- Query：使用最近选择的 Introduction 简版/详版及当前语言原文，解答概念、公式、推导与思考题。范围包括理解教材所需的补充知识，不限于原文逐字出现的知识。正文包含 answer、reasoning、learning_check 三个小节，不依赖预测结果。
- Prediction：以最近完成的预测数据及模型解释知识为依据，正文包含 observations、prediction_summary、consistency、reliability、next_steps、uncertainty 六个小节。区分回归输出与守恒计算，追加范围/不确定性提醒；没有预测时先提示完成预测。

两个对话框历史独立，新预测清空旧分析对话。最多传入最近 12 条历史，单条与当前问题各最多 4000 字符。已通过输入检查的问题在后续生成失败时仍可用于追问；失败或被拦截的候选回答不进入后续上下文，无关问题也不进入。

## 生成与审核

正文使用 response_format=text，按固定英文小节标识输出 Markdown，由应用解析成所需字段并显示中英文标签。数学公式使用 $...$ 或 $$...$$，LaTeX 保留原始反斜杠，避免长公式嵌入 JSON 导致转义错误。旧的合法 JSON 对象也可被解析，但不会修复或猜测非法 JSON 内容。

输入和输出范围判断仍使用 JSON。输入判断为相关、澄清、拒绝或转到另一板块。输出审核允许相关推导、符号解释、例子和积分假设，不能仅因排版、详略或非逐字引用教材而拦截。判为 block 时必须提供 reason（off_topic/unsafe/injection）和来自候选回答的确切原文 evidence。程序验证证据确实存在；不能只返回无依据的 block。

无有效证据的输出拦截会自动复核一次；复核 allow 才显示回答，有有效证据的 block 继续拦截；复核仍无依据则显示 REVIEW_EVIDENCE，明确这不意味着用户的问题无关。没有跳过审核的直接放行逻辑。范围判断仍依赖模型，不能保证误拦截率为零，也不构成科学正确性保证。

生成正文为空或小节格式错误时，最多重新生成一次，仍须经过完整审核。鉴权、付费、限流和截断错误不自动重试。通常每次回答 3 个 API 请求；若同时触发正文恢复和审核复核，最多 5 个，请求用量和延迟相应增加。前端等待后端 /chat 的读取超时为 300 秒。

官方 DeepSeek V4 调用显式设置 thinking.type=disabled，避免默认思考模式耗尽短输出额度。输入审核上限 512 tokens，正文 2400，输出审核 768。其他服务不附加 DeepSeek 专用参数。frontend/chat_formatting.py 在显示时兼容 LaTeX 圆括号/方括号分隔符，不改公式内容或代码块。

## 诊断和部署更新

错误包含 error_stage、error_code 及适用时的 HTTP 状态，日志只记录本地阶段/代码/状态，不记录密钥、用户正文或模型响应内容。常见代码：

- AUTH_FAILED / PAYMENT_REQUIRED / RATE_LIMIT：鉴权、付款额度或限流问题。
- OUTPUT_TRUNCATED / THINKING_ONLY / EMPTY_CONTENT：截断、仅思考内容或空正文。
- ANSWER_FORMAT / ANSWER_SCHEMA：正文结构不合格。
- INVALID_JSON / INVALID_SCOPE：范围审核响应格式错误。
- REVIEW_EVIDENCE：输出审核复核后仍未给出有效依据，候选回答未展示。

frontend/tutor_client.py 按当前 backend/tutor.py 源码内容加载模块并校验接口版本，避免 Streamlit 长驻进程缓存旧函数导致 unexpected keyword argument learning_context。发布时提交整个改动集，包含新模块；仅刷新浏览器不等于重启服务进程。Docker 前端复制完整 frontend，以及 backend/tutor.py 和 tutor_knowledge.md。

## 预测模型边界

当前模型为 pH 3–8、按最近 pH 路由的单 a* GBR。模型文件哈希用于版本标识，外部测试指标来自模型包。confidence 为 pH 启发式评分，不是准确概率；训练浓度范围与颜色分布元数据缺失时显示未知。质量守恒残差按显示截断后的浓度计算，代数守恒不证明预测准确。输入允许 pH 0–14 以报告域外情况，实际训练有效范围仍为 3–8。

## 验证

从仓库根目录运行：python -m unittest discover -s backend -p "test_*.py"。

当前 33 项离线测试通过，并用 Streamlit AppTest 模拟截图中的微分/积分关系提问，验证 Markdown 公式传输、无依据拦截的复核与页面显示。测试提供模拟模型响应，不代表真实模型分类准确率。未使用真实密钥调用验证，当前修复尚未部署。

官方参数说明：https://api-docs.deepseek.com/api/create-chat-completion/ 、https://api-docs.deepseek.com/guides/thinking_mode/ 、https://api-docs.deepseek.com/guides/json_mode/ 。
