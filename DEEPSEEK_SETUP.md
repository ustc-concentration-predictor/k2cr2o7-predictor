# DeepSeek 接入与当前检查结果

入口为 `frontend/app.py`。在 Streamlit Cloud 的应用设置 Secrets 中粘贴 `.streamlit/secrets.toml.example` 内容，替换 key 和实际后端地址。本地从仓库根目录启动时保存为 `.streamlit/secrets.toml`；从 frontend 启动则保存到 frontend/.streamlit/secrets.toml。不要提交真实 key。

Streamlit 服务端读取 LLM_API_KEY 时直接调用 DeepSeek，使用 backend/tutor.py；不会把 key 传给预测后端或浏览器。仓库部署必须包含 backend/tutor.py 和 backend/tutor_knowledge.md。未配置 Streamlit key 时保留 `/chat` 后端调用；独立后端需另外设置 LLM_API_KEY、LLM_BASE_URL、LLM_MODEL 环境变量。Streamlit Secrets 不会自动同步到 Render。

API_BASE_URL 指向 FastAPI；DeepSeek 只负责问答，不替代图像预测服务。现有 `/predict`、`/predict/base64`、`/health`、`/model/info` 和 `/chat` 路由均已存在。health 的 model_loaded 表示模型加载，chat_configured 仅表示后端有 key，不证明 key 可用，也不反映 Streamlit 直连状态。

导师 harness 包括教学知识文件、受限系统规则、用户/助手历史白名单、输入长度限制、六字段 JSON 输出校验、错误安全回退、固定不确定性说明和范围提醒。数值由预测服务提供，大模型负责解释。提示词安全约束不能保证拦截所有不安全或错误生成；当前没有独立语义安全分类器，仍需真实模型教学评测。

模型是 pH 3–8、最近 pH 路由的单 a* GBR，并非旧 README 描述的 RF / pH 2–12。已加入模型文件哈希版本、真实外部测试指标、浓度表与按 Cr 计的堆叠图，修复截断后质量守恒残差。原 confidence 是 pH 启发式分数，界面已取消概率表述。

仍缺模型包中的训练浓度范围与 a* 分布边界，因此不能实现经验证的特征距离置信提示；显示未知并提示咨询教师。需补入可追溯的训练元数据才能继续完成该部分，不能用旧 README 的范围替代。pH 为必填，填写后才能上传；允许 0–14 以便报告域外情况，训练有效范围仍为 3–8。

本次只修改本地项目，未部署线上；未使用真实 key 进行付费调用。

官方配置依据：https://api-docs.deepseek.com/ 和 https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management 。模型名称可按账户可用模型修改。

验证：5 项离线回归测试通过，Python 编译与 git diff --check 通过；Streamlit AppTest 预测页无异常、显示 7 个指标和 2 个表格。
