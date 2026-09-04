# DeepSeek 接入与当前检查结果

入口为 `frontend/app.py`。在 Streamlit Cloud 的应用设置 Secrets 中粘贴 `.streamlit/secrets.toml.example` 内容，替换 key 和实际后端地址。本地从仓库根目录启动时保存为 `.streamlit/secrets.toml`；从 frontend 启动则保存到 frontend/.streamlit/secrets.toml。不要提交真实 key。

Streamlit 服务端读取 LLM_API_KEY 时直接调用 DeepSeek，使用 backend/tutor.py；不会把 key 传给预测后端或浏览器。仓库部署必须包含 backend/tutor.py 和 backend/tutor_knowledge.md。未配置 Streamlit key 时保留 `/chat` 后端调用；独立后端需另外设置 LLM_API_KEY、LLM_BASE_URL、LLM_MODEL 环境变量。Streamlit Secrets 不会自动同步到 Render。

API_BASE_URL 指向 FastAPI；DeepSeek 只负责问答，不替代图像预测服务。现有 `/predict`、`/predict/base64`、`/health`、`/model/info` 和 `/chat` 路由均已存在。health 的 model_loaded 表示模型加载，chat_configured 仅表示后端有 key，不证明 key 可用，也不反映 Streamlit 直连状态。

两个对话框使用独立 harness，共用 API 传输、用户/助手历史白名单、长度限制与异常回退。

- Query：读取用户最近选择的 Introduction 简版/详版与当前语言的原文，作为 learning_context 传入；使用学习辅导系统规则，按 answer、reasoning、learning_check 三字段校验回复。围绕教材概念、公式、思考题解惑，不依赖预测结果，不附预测专用免责声明。
- Prediction：仅使用最近完成预测的结构化结果及模型解释知识，按 observations、prediction_summary、consistency、reliability、next_steps、uncertainty 六字段校验回复。评估回归输出、守恒一致性、模型指标和适用范围，追加不确定性与范围提醒；缺少结果时不调用大模型。

两处对话历史分开保存，新预测会清空旧分析对话。页面切换保留 Introduction 版本；API 的 learning_context 和 language 字段让后端转发路径与 Streamlit 直连行为一致。数值由预测服务提供，大模型负责解释。新增话题范围检查：先以独立模型调用判定 allow、clarify、off_topic 或转向另一板块。只有 allow 才继续生成；回答通过该板块 JSON 结构校验后，再独立调用模型检查回答是否跑题。检查返回非法结果或服务失败时不展示未审核候选回答，不绕过检查。拒绝、澄清、引导均使用程序固定的中英文文案。

明显无关或混合无关任务的请求停止生成；模糊问题先澄清；相关追问会带上最近对话辅助判断。界面保留被拒绝的对话记录，但后续请求不携带这些记录。检查状态通过后端 ChatResponse 传回，Streamlit 直连和后端转发均经过同一检查流程。缺少预测结果时先判断板块范围，相关预测请求再提示先预测。

正常回答通常需要 3 次 API 调用（输入检查、生成、输出检查）；拒绝/澄清/引导通常只需 1 次，延迟和用量相应增加。范围检查使用同一已配置模型的独立调用，不是确定性语义规则；测试验证了流程拦截和错误回退，没有证明真实模型的分类准确率。仍需真实模型教学与安全评测，不能保证拦截所有偏题、不安全或科学错误内容。

模型是 pH 3–8、最近 pH 路由的单 a* GBR，并非旧 README 描述的 RF / pH 2–12。已加入模型文件哈希版本、真实外部测试指标、浓度表与按 Cr 计的堆叠图，修复截断后质量守恒残差。原 confidence 是 pH 启发式分数，界面已取消概率表述。

仍缺模型包中的训练浓度范围与 a* 分布边界，因此不能实现经验证的特征距离置信提示；显示未知并提示咨询教师。需补入可追溯的训练元数据才能继续完成该部分，不能用旧 README 的范围替代。pH 为必填，填写后才能上传；允许 0–14 以便报告域外情况，训练有效范围仍为 3–8。

本次只修改本地项目，未部署线上；未使用真实 key 进行付费调用。

官方配置依据：https://api-docs.deepseek.com/ 和 https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management 。模型名称可按账户可用模型修改。

验证：13 项离线回归测试通过（提供模拟分类结果，验证程序分支与失败处理）；Streamlit AppTest 检查简版/详版选择跨页面保留、中英文教材切换、Query 请求携带正确原文及后端转发；另验证拒绝记录在页面可见、后续请求排除这些记录及 API 保留范围检查状态；Python 编译与 git diff --check 通过。


## 更新后 Query 出现 TypeError

若报错停在 frontend/app.py 的 ask_tutor 调用处，且服务日志提示 unexpected keyword argument learning_context，常见原因是 Streamlit 长驻进程仍缓存旧版 tutor 模块。可先在应用管理页重启整个应用，再重试；仅刷新浏览器不会重建服务进程。

frontend/tutor_client.py 现在按 backend/tutor.py 的确切源码内容缓存并加载独立模块，避免复用旧的全局 tutor 模块；HARNESS_API_VERSION 与函数签名在调用前校验。不兼容时显示维护提示，不删除新参数或降级到缺少范围检查的旧接口。发布时须同时包含 frontend/tutor_client.py、frontend/app.py 和 backend/tutor.py。

回归验证：复现旧接口缓存时的同位置 TypeError；修复后同一 Streamlit AppTest 场景成功完成输入检查、生成和输出检查。17 项离线测试通过。尚未连接线上应用日志，因此缓存原因与用户提供的调用栈一致，但不能仅凭已脱敏信息排除其他 TypeError 来源。


## DeepSeek JSON 调用与错误诊断

用户确认的配置是 LLM_BASE_URL=https://api.deepseek.com、LLM_MODEL=deepseek-v4-flash、API_BASE_URL=https://k2cr2o7-api-om9i.onrender.com。后端地址以该值为准；旧 README 中不含 -om9i 的地址不能作为本部署依据。

DeepSeek V4 默认开启思考模式，原来的范围检查 max_tokens=160 可能在输出最终 JSON 前耗尽。现在对官方 api.deepseek.com 的 V4 调用显式设置 thinking.type=disabled，范围检查额度为 512，正文额度为 2400；不向其他服务发送 DeepSeek 专用参数。空答案、思考内容但无最终答案、finish_reason=length、HTTP 错误和 schema 错误分别诊断，失败仍不跳过范围检查，正文 EMPTY_CONTENT 时最多自动重试一次，其余错误不自动重试。

Secrets 应填写纯 URL。代码兼容粘贴的 Markdown 链接外壳，并对无效 LLM_BASE_URL 给出 INVALID_ENDPOINT 提示。范围审核 JSON 示例改为实际的单个 decision 值，避免模型照抄竖线分隔的候选值。

页面及 API 返回 error_stage、error_code 和必要的 HTTP 状态。阶段为 configuration、input_scope、generation、answer_format、output_scope；日志仅记录这些本地阶段/代码与状态，不记录密钥、问题、推理内容或服务商响应正文。示例：AUTH_FAILED 表示鉴权失败，PAYMENT_REQUIRED 表示付款/额度问题，OUTPUT_TRUNCATED 表示输出截断，INVALID_SCOPE 表示范围判断格式无效。

依据：https://api-docs.deepseek.com/guides/thinking_mode/ 和 https://api-docs.deepseek.com/api/create-chat-completion/ 。本轮 24 项离线测试以及使用上述配置的模拟 Streamlit 调用通过；未验证真实密钥调用，也未部署这些修复。


## 教材追问、公式渲染与空答案恢复

截图中的 generation/EMPTY_CONTENT 表示生成阶段没有返回最终答案。现对这一错误且仅这一阶段增加一次重试，修改系统提示要求返回非空 JSON；重试结果仍经过 schema 与输出范围检查。连续两次为空即停止，鉴权/付款/限流/截断/格式错误不走该恢复流程。通常仍为三次调用，触发恢复时最多四次；可能增加一次 API 用量。后端转发的客户端读取等待调整为 240 秒以容纳恢复流程。

范围规则明确覆盖整篇教材及必要数学，允许范特霍夫公式、温度和平衡、符号/变化率讲解、例子和自检题；“没看懂”不作为范围不明确的理由。输出审核不再将公式排版、详略、措辞或非逐字引用当作偏题。仍拒绝实质无关任务和危险操作。这是提示与判断流程的调整，尚未测量真实模型误拦截率。

frontend/chat_formatting.py 将助手回答中的 LaTeX 方括号/圆括号分隔符转为 Streamlit 支持的美元符号数学分隔符，保留命令、代码块和原始公式；历史回答也在显示时转换。教材原文未改写。生成规则要求用规范数学排版，并在学生表示不理解时拆解符号与含义，而非只重复公式。

用户问题通过输入检查后，即使后续生成/审核失败，也保留该问题用于相关追问；失败或被拦截的候选回答不传入后续上下文。无关问题仍不传入。

本轮 29 项离线测试与模拟 Streamlit 页面检查通过，包括空答案恢复、恢复次数上限、恢复后继续审核、公式分隔符转换与上下文保留。未进行真实密钥调用，修复尚未部署。
