"""Bilingual UI strings for the Streamlit frontend."""

from __future__ import annotations

from typing import Dict


UI_TEXT: Dict[str, Dict[str, str]] = {
    "en": {
        'learning_tutor_info': 'Ask about concepts, equations, or exercises in Introduction. Answers use the selected reading as context.',
        'prediction_tutor_info': 'Assess the latest prediction: species estimates, mass balance, model applicability, uncertainty, and suggested checks.',
        'learning_source': 'Reading context: Introduction · {version}',
        'tutor_info': 'The teaching tutor supports Streamlit Secrets or backend API configuration; replies distinguish observations, predictions, calculations, and inferences.',
        'heuristic_score': 'pH heuristic score (not an accuracy probability)',
        'required_ph': 'Sample pH (required)',
        'ph_first': 'Enter the sample pH before uploading. The model routes to the nearest trained pH.',
        'last_prediction_note': 'Last completed prediction (pH {ph:g}). Click Predict again after changing the image or pH.',
        "sidebar_subtitle": "Chromium(VI) species predictor",
        "language": "Language / 语言",
        "module": "Module",
        "module_introduction": "Introduction",
        "module_query": "Query",
        "module_prediction": "Model Prediction",
        "backend_online": "Backend online",
        "backend_offline": "Backend offline",
        "recent_predictions": "Recent predictions",
        "introduction": "Introduction",
        "introduction_version": "Introduction version",
        "simple": "Brief",
        "detailed": "Detailed",
        "intro_missing": "Introduction content is missing.",
        "ask_more": "I still have questions",
        "start_prediction": "Start the experiment",
        "query": "Query",
        "backend": "Backend",
        "online": "online",
        "offline": "offline",
        "general_query": 'Introduction learning assistant',
        "query_placeholder": 'Which concept, equation, or exercise in Introduction is confusing? You can paste the passage here.',
        "llm_unconfigured": (
            "The AI assistant is ready to connect. Configure the backend "
            "environment variables to enable it."
        ),
        "message": "Message",
        "send": "Send",
        "waiting_model": "Waiting for model response...",
        "chat_api_error": "Chat API error",
        "chat_unavailable": "Chat API unavailable",
        "api_error": "API error",
        "prediction": "Model Prediction",
        "workflow": (
            "Workflow: upload an ROI image and pH, standardize illumination, "
            "extract the Lab a feature, directly predict HCrO₄⁻, Cr₂O₇²⁻, "
            "and CrO₄²⁻, then compute total Cr(VI) by mass balance."
        ),
        "sample_image": "Sample image",
        "select_photo": "Select photo",
        "training_note": (
            "The deployed Ka₂=3.0×10⁻⁷ model is trained for pH 3–8. "
            "Total Cr(VI) is calculated from the three predicted species."
        ),
        "predict": "Predict",
        "analyzing": "Analyzing ROI image...",
        "roi_preview": "ROI preview",
        "selected_roi": "Selected ROI",
        "draw_roi": "Draw a box around the cuvette region.",
        "upload_first": "Upload a photo, then select the cuvette region.",
        "equilibrium_basis": "Equilibrium basis",
        "prediction_completed": "Prediction completed.",
        "estimated_total": "Calculated total Cr(VI)",
        "confidence": "Confidence",
        "mass_balance_residual": "Mass-balance residual",
        "result_assistant": 'Prediction assessment assistant',
        "result_placeholder": 'Ask about the latest prediction, mass-balance consistency, model applicability, or how to check its reliability.',
        "footer": (
            "K₂Cr₂O₇ Prediction System · ML species prediction with "
            "equilibrium calculation"
        ),
        "sim_title": "Interactive Cr(VI) equilibrium simulator",
        "sim_initial": "Initial solution: 5 mM K₂Cr₂O₇, about 50 mL",
        "ph_meter": "pH meter",
        "acid": "acid",
        "basic": "basic",
        "alkaline": "alkaline",
        "ions": "ions",
        "ph_electrode": "pH electrode",
        "sim_note": (
            "pH is limited to 1.0–14.0. Solution color is visually enhanced "
            "from the 5 mM training colors."
        ),
    },
    "zh": {
        'learning_tutor_info': '帮助理解 Introduction 中的概念、公式和思考题，结合当前所选教材解答。',
        'prediction_tutor_info': '分析最近一次预测的物种浓度、守恒一致性、模型适用性与不确定性，并给出核查建议。',
        'learning_source': '当前学习资料：Introduction · {version}',
        'tutor_info': '教学导师支持 Streamlit Secrets 或后端 API 配置；回答区分观察、预测、计算与推断。',
        'heuristic_score': 'pH 范围规则评分（非准确概率）',
        'required_ph': '样本 pH（必填）',
        'ph_first': '请先确认样本 pH，再上传图像。模型以最近训练 pH 路由。',
        'last_prediction_note': '以下为上一次完成的预测（pH {ph:g}），修改图像或 pH 后需重新点击 Predict。',
        "sidebar_subtitle": "铬(VI)物种浓度预测",
        "language": "语言 / Language",
        "module": "功能模块",
        "module_introduction": "知识引入",
        "module_query": "化学问答",
        "module_prediction": "模型预测",
        "backend_online": "后端在线",
        "backend_offline": "后端离线",
        "recent_predictions": "最近预测",
        "introduction": "知识引入",
        "introduction_version": "内容版本",
        "simple": "简版",
        "detailed": "详版",
        "intro_missing": "知识引入内容文件缺失。",
        "ask_more": "我对知识点还有疑问",
        "start_prediction": "开始实验预测",
        "query": "化学问答",
        "backend": "后端",
        "online": "在线",
        "offline": "离线",
        "general_query": 'Introduction 学习助手',
        "query_placeholder": 'Introduction 中哪个概念、公式或思考题不明白？可以粘贴具体段落。',
        "llm_unconfigured": "大模型接口已预留；配置后端环境变量后即可使用。",
        "message": "消息",
        "send": "发送",
        "waiting_model": "正在等待模型回答……",
        "chat_api_error": "问答接口错误",
        "chat_unavailable": "问答接口不可用",
        "api_error": "预测接口错误",
        "prediction": "模型预测",
        "workflow": (
            "流程：上传感兴趣区域（ROI）图像并输入 pH，进行光照标准化，"
            "提取 Lab a 特征，直接预测 HCrO₄⁻、Cr₂O₇²⁻ 和 CrO₄²⁻，"
            "再依据铬元素质量守恒计算总 Cr(VI)。"
        ),
        "sample_image": "样品图像",
        "select_photo": "选择样品照片",
        "training_note": "当前为 Ka₂=3.0×10⁻⁷ 模型，训练范围为 pH 3–8；总 Cr(VI) 由三个直接预测物种计算。",
        "predict": "开始预测",
        "analyzing": "正在分析所选图像区域……",
        "roi_preview": "感兴趣区域预览",
        "selected_roi": "已选择的感兴趣区域",
        "draw_roi": "请框选比色皿所在区域。",
        "upload_first": "请先上传照片，再框选比色皿区域。",
        "equilibrium_basis": "平衡计算依据",
        "prediction_completed": "预测完成。",
        "estimated_total": "守恒计算总 Cr(VI)",
        "confidence": "置信度",
        "mass_balance_residual": "物料衡算残差",
        "result_assistant": '预测结果评估助手',
        "result_placeholder": '询问本次预测的物种结果、守恒一致性、适用范围，或如何核查可靠性。',
        "footer": "K₂Cr₂O₇ 浓度预测系统 · 机器学习物种预测与平衡计算",
        "sim_title": "Cr(VI) 平衡交互模拟器",
        "sim_initial": "初始溶液：5 mM K₂Cr₂O₇，约 50 mL",
        "ph_meter": "pH 计",
        "acid": "加酸",
        "basic": "碱性",
        "alkaline": "加碱",
        "ions": "离子浓度",
        "ph_electrode": "pH 电极",
        "sim_note": "pH 范围限制为 1.0–14.0；溶液颜色由 5 mM 训练色彩进行视觉增强。",
    },
}


def text(lang: str, key: str) -> str:
    """Return a localized UI string."""
    return UI_TEXT.get(lang, UI_TEXT["en"]).get(key, key)
