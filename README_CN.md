# 🧪 重铬酸钾浓度预测系统

**[English](./README.md) | 中文**

---

基于图像颜色分析与机器学习的溶液浓度智能检测工具

---

## 🌐 在线演示

- **前端界面**: https://k2cr2o7-predictor.vercel.app
- **API 文档**: https://k2cr2o7-api.onrender.com/docs

---

## ✨ 功能特点

- 📷 上传比色皿照片即可预测浓度
- 🎨 自动提取 RGB/HSV/Lab 颜色特征
- 📊 实时显示预测结果与置信度
- 🔬 模型训练 pH 范围为 3-8；范围外输入仅用于提示域外风险
- 📱 响应式网页设计
- 💯 完全免费部署

---

## 🚀 快速开始

### 使用在线版本

直接访问 https://k2cr2o7-predictor.vercel.app 即可使用，无需安装任何软件。

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/yourusername/k2cr2o7-predictor.git
cd k2cr2o7-predictor

# 安装依赖并启动后端
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# 安装依赖并启动前端（新终端）
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

访问: http://localhost:8501

---

## 📖 使用说明

1. 打开网页，上传已裁剪好的比色皿照片
2. 输入溶液的 pH 值（模型训练范围为 3-8）
3. 点击"预测"按钮
4. 查看浓度结果、置信度和各组分浓度

**⚠️ 注意**: pH 超出 3-8 时属于模型训练范围外预测，应谨慎解释。

### 拍摄建议

- 使用均匀的自然光或白光
- 白色背景（如白纸）
- 确保比色皿清晰可见
- 避免阴影和反光
- 上传前裁剪至比色皿区域

---

## 🏗️ 技术架构

```
前端 (Streamlit) ←→ 后端 (FastAPI) ←→ 分 pH 的 GradientBoostingRegressor
     Vercel              Render              Joblib
```

### 模型信息

- **类型**: 分 pH 子模型的 GradientBoostingRegressor
- **特征**: Lab `a*`；pH 用于路由到最近的训练子模型
- **平衡常数**: K₂ = 3.0×10⁻⁷
- **直接预测**: HCrO₄⁻、Cr₂O₇²⁻、CrO₄²⁻
- **守恒计算**: 总 Cr(VI) = HCrO₄⁻ + 2×Cr₂O₇²⁻ + CrO₄²⁻
- **适用范围**: pH 3-8；性能指标以模型包和 `/model/info` 为准

---

## 🆓 免费部署

本项目可以完全免费部署：

- **前端**: [Vercel](https://vercel.com) (免费版)
- **后端**: [Render](https://render.com) (免费版)
- **存储**: [GitHub](https://github.com) (免费版)

详细部署步骤: [DEPLOY_CLOUD.md](./DEPLOY_CLOUD.md)

---

## 📁 项目结构

```
.
├── backend/              # 后端
│   ├── main.py           # API 主入口
│   ├── image_processor.py # 图像预处理
│   ├── model.py          # 模型封装
│   ├── requirements.txt  # Python 依赖
│   └── models/
│       └── RF_model.joblib  # 训练好的模型
├── frontend/             # 前端
│   ├── app.py            # Web 界面
│   └── requirements.txt  # Python 依赖
├── docker/               # Docker 配置
│   ├── docker-compose.yml
│   ├── Dockerfile.backend
│   └── Dockerfile.frontend
├── README.md             # 英文版本
├── README_CN.md          # 本文件（中文）
├── LICENSE               # 许可证
├── render.yaml           # Render 部署配置
└── vercel.json           # Vercel 部署配置
```

---

## 🔬 化学原理

重铬酸钾体系存在酸碱平衡：

```
2CrO₄²⁻ (黄色) + 2H⁺ ⇌ Cr₂O₇²⁻ (橙色) + H₂O
```

溶液颜色随 pH 变化，通过机器学习建立颜色-浓度关系模型。

---

## 🛠️ 技术栈

- **后端**: FastAPI, OpenCV, scikit-learn, NumPy
- **前端**: Streamlit, Pillow, Requests
- **部署**: Vercel, Render, Docker

---

## 📄 许可证

MIT License

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 🙏 致谢

- 机器学习模型: [scikit-learn](https://scikit-learn.org)
- Web 框架: [FastAPI](https://fastapi.tiangolo.com), [Streamlit](https://streamlit.io)
- 部署平台: [Vercel](https://vercel.com), [Render](https://render.com)

---

## 📧 联系方式

如有问题或建议，请通过 GitHub Issues 联系我们。
