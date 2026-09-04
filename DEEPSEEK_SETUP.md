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
