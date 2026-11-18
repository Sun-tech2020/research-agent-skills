import os
import fitz
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")
model = os.getenv("SMART_LLM", "glm-4-flash").replace("openai:", "")

client = OpenAI(
    api_key=api_key,
    base_url=api_base
)

target_dir = "/Users/scottsun/Documents/Obsidian Vault/参考文献/基差与泡沫/研究方法"

pdfs = [f for f in os.listdir(target_dir) if f.endswith(".pdf")]

details_md = "# 文献详情拆解：方法论篇\n\n"

for pdf in pdfs:
    print(f"Processing {pdf}...")
    pdf_path = os.path.join(target_dir, pdf)
    
    # Extract text
    doc = fitz.open(pdf_path)
    text = ""
    # We read first 15 pages
    for i in range(min(15, len(doc))):
        text += doc[i].get_text()
    
    prompt = f"""请分析以下文献的部分文本（主要包含标题、摘要和方法论部分），并严格按照以下格式提取信息：

标题与本地链接：[[{pdf}]]
关键词：提取3-5个核心关键词
核心内容：
- 具体的计量模型公式：请提取文中使用到的 Rolling Fama Regression 或 TVP-VAR 相关的核心计量模型公式。必须使用 $$ 独立公式包裹或 $ 行内公式包裹，严禁使用 ```latex 。
- 数据来源：文献中使用的数据集、频次及来源。
- 应用逻辑：该模型是如何在商品期货、价格发现、基差偏离或泡沫识别中被应用的。

文献文本内容片段如下：
{text[:15000]}

请直接返回 Markdown 格式的内容，不要使用 ```markdown 外层包裹。
"""
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一位专业的金融计量学研究助理。严禁使用 ```latex 包裹公式，独立公式只能用 $$ 包裹。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    result = response.choices[0].message.content
    
    # Double check formatting
    result = re.sub(r'```latex\n(.*?)\n```', r'$$\n\1\n$$', result, flags=re.DOTALL)
    result = re.sub(r'```markdown\n(.*?)\n```', r'\1', result, flags=re.DOTALL)
    result = re.sub(r'\\\((.*?)\\\)', r'$\1$', result)
    result = re.sub(r'\\\[(.*?)\\\]', r'$$\n\1\n$$', result, flags=re.DOTALL)
    
    details_md += f"## {pdf}\n\n{result}\n\n---\n\n"

details_path = os.path.join(target_dir, "文献详情拆解_方法论篇.md")
with open(details_path, "w", encoding="utf-8") as f:
    f.write(details_md)
print(f"Saved {details_path}")

print("Generating comprehensive review...")

review_prompt = f"""基于以下整理的文献详情，请生成一份名为《方法论深度综述》的独立文档。

要求：
1. 以专业学术综述的口吻撰写。
2. 总结目前利用“滚动 Fama 回归”和“TVP-VAR”识别商品期货价格泡沫的技术路径。
3. 重点分析这些方法在处理“基差偏离”（Basis Deviation）时的优势与局限性。
4. 内容应包括：引言、滚动Fama回归技术路径及基差偏离处理能力、TVP-VAR技术路径及基差偏离处理能力、比较与结论。
5. 请使用 Markdown 格式。公式必须使用 $$ 独立公式包裹或 $ 行内公式包裹，严禁使用 ```latex 。

文献详情材料：
{details_md}
"""

response_review = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "你是一位资深的金融学术研究员。严禁使用 ```latex 包裹公式，必须使用 $$ 或 $。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.5
)

review_md = response_review.choices[0].message.content
review_md = re.sub(r'```latex\n(.*?)\n```', r'$$\n\1\n$$', review_md, flags=re.DOTALL)
review_md = re.sub(r'```markdown\n(.*?)\n```', r'\1', review_md, flags=re.DOTALL)
review_md = re.sub(r'\\\((.*?)\\\)', r'$\1$', review_md)
review_md = re.sub(r'\\\[(.*?)\\\]', r'$$\n\1\n$$', review_md, flags=re.DOTALL)

review_path = os.path.join(target_dir, "方法论深度综述.md")
with open(review_path, "w", encoding="utf-8") as f:
    f.write(review_md)

print(f"Saved {review_path}")
print("All tasks completed.")
