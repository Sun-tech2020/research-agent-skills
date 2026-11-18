# Research Agent Skills (科研 Agent 全流程技能矩阵)

一套面向经济金融、大宗商品、前沿产业与社会科学领域的**自主科研智能体技能矩阵（Agent Skills Pipeline）**。覆盖从选题大纲策划、文献高保真检索抓取、跨学科文献综述合成、微观计量与物理模型构建，到顶级同行评议规范学术论文生成的端到端科研工作流。

---

## 🌟 核心技能矩阵 (Skills Architecture)

本项目将复杂的学术科研任务拆解为高内聚、原子化、确定性的智能体技能链条，位于 `skills/` 目录：

| 阶段 | 技能文件 | 功能描述 |
| :--- | :--- | :--- |
| **Stage 1: 课题策划与蓝图** | `1.1 Outline_Generator.skill` | 科学化解构研究问题，生成多级学术大纲与技术路线图。 |
| | `1.2 Blueprint_to_Theoretical_Constraint.skill` | 将宏观研究蓝图映射为微观理论假设与数学/经济学硬约束。 |
| **Stage 2: 文献工程与全景综述** | `2.1 Literature_Capturer.skill` | 跨数据源自动化抓取高权威论文原文、生成高保真下载存证清单。 |
| | `2.2 Reviewer_Blueprint.skill` | 顶级期刊审稿人视角的文献评价蓝图与批判性分析。 |
| | `2.3 Literature_Review_Synthesizer.skill` | **(v5.3.0)** 严格执行原子单引协议（Atomic Single Citation Protocol），杜绝引用混淆堆叠，结构化生成全景文献综述。 |
| **Stage 3: 实证建模与机制检验** | `3.2 Empirical_Modeler.skill` | 计量与数学建模方案构建（GSADF时变泡沫检验、LPPL临界崩溃相变、SVAR供求结构分解等）。 |
| | `3.3 Empirical_Result_Synthesizer.skill` | 高维度实证结果自动化解读、三线表规范生成与经济学因果归因。 |
| **Stage 4: 学术论文全真生成** | `4.1 Academic_Paper_Generator.skill` | **(v5.13.0)** 顶级同行评议规范正文生成，强制图表三线表、零幻视公式与严格的一对一引用校验。 |
| | `4.2 Format_Standard.skill` | **(v3.3.0)** 期刊排版格式、行内引用语法与交叉标引强制约束。 |
| **总控中枢** | `Research_Pipeline_Matrix_Engine.skill` | 端到端全流程调度引擎，串联流水线各阶段的输入输出流。 |

---

## 🚀 快速上手 (Quick Start)

### 1. 克隆仓库
```bash
git clone https://github.com/Sun-tech2020/research-agent-skills.git
cd research-agent-skills
```

### 2. 环境安装
推荐使用 Python 3.10+：
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量
复制环境配置模板并填写你的大模型或搜索引擎 API Key：
```bash
cp .env.example .env
```
用编辑器打开 `.env` 并按需填入你的密钥：
* `OPENAI_API_KEY`: 智谱 GLM 或其他 OpenAI 兼容的 API Key
* `TAVILY_API_KEY`: 联网文献检索工具 Key（可选）

### 4. 使用方式
* **在 Antigravity / Cursor / Claude Code 等智能体平台中使用**：
  将 `skills/` 目录挂载或复制到你的 Agent 技能加载目录中，Agent 即可自动调用全流程科研技能。
* **本地辅助脚本运行**：
  ```bash
  python generate_reviews.py  # 自动化提取文献要点与元数据
  python fix_markdown.py      # 学术 Markdown 格式与排版自动化规范修正
  ```

---

## 🔒 安全与合规说明

* 本仓库严格遵循开源安全与隐私保护规范，不包含任何真实 API 密钥与内部私有课题数据。
* 敏感环境变量与本地缓存已由 `.gitignore` 全面拦截。

---

## 📄 License
MIT License
