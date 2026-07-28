"""Bilingual UI strings for the Streamlit frontend."""

from __future__ import annotations

from typing import Dict


UI_TEXT: Dict[str, Dict[str, str]] = {
    "en": {
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
        "general_query": "General chemistry query",
        "query_placeholder": (
            "Ask about dichromate equilibrium, experimental design, "
            "or model interpretation..."
        ),
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
            "extract the Lab a feature, predict total Cr(VI), HCrO₄⁻, and "
            "Cr₂O₇²⁻, then compute CrO₄²⁻ by mass balance."
        ),
        "sample_image": "Sample image",
        "select_photo": "Select photo",
        "training_note": (
            "The deployed model is trained for pH 3–8. At pH 7–8, "
            "CrO₄²⁻ uncertainty may be amplified."
        ),
        "predict": "Predict",
        "analyzing": "Analyzing ROI image...",
        "roi_preview": "ROI preview",
        "selected_roi": "Selected ROI",
        "draw_roi": "Draw a box around the cuvette region.",
        "upload_first": "Upload a photo, then select the cuvette region.",
        "equilibrium_basis": "Equilibrium basis",
        "prediction_completed": "Prediction completed.",
        "estimated_total": "Estimated total Cr(VI)",
        "confidence": "Confidence",
        "mass_balance_residual": "Mass-balance residual",
        "result_assistant": "Result analysis assistant",
        "result_placeholder": (
            "Ask the model to summarize this result, discuss reliability, "
            "or suggest experimental checks..."
        ),
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
        "general_query": "通用化学问答",
        "query_placeholder": "可询问重铬酸盐平衡、实验设计或模型结果解释……",
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
            "提取 Lab a 特征，预测总 Cr(VI)、HCrO₄⁻ 和 Cr₂O₇²⁻，"
            "再依据物料衡算计算 CrO₄²⁻。"
        ),
        "sample_image": "样品图像",
        "select_photo": "选择样品照片",
        "training_note": "当前模型的训练范围为 pH 3–8；在 pH 7–8 时，CrO₄²⁻ 的不确定性可能增大。",
        "predict": "开始预测",
        "analyzing": "正在分析所选图像区域……",
        "roi_preview": "感兴趣区域预览",
        "selected_roi": "已选择的感兴趣区域",
        "draw_roi": "请框选比色皿所在区域。",
        "upload_first": "请先上传照片，再框选比色皿区域。",
        "equilibrium_basis": "平衡计算依据",
        "prediction_completed": "预测完成。",
        "estimated_total": "估算总 Cr(VI)",
        "confidence": "置信度",
        "mass_balance_residual": "物料衡算残差",
        "result_assistant": "结果分析助手",
        "result_placeholder": "可要求模型总结结果、讨论可靠性或提出实验核验建议……",
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
