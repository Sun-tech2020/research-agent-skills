import os
import re

dir_path = "/Users/scottsun/Documents/Obsidian Vault/参考文献/基差与泡沫/研究方法"
files = ["文献详情拆解_方法论篇.md", "方法论深度综述.md"]

for file in files:
    path = os.path.join(dir_path, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove ```markdown and ```
    content = re.sub(r'```markdown\n', '', content)
    content = re.sub(r'\n```\n', '\n', content)
    # also remove leftover ``` if any
    content = re.sub(r'^```\s*$', '', content, flags=re.MULTILINE)

    # Replace ```latex ... ``` with $$ ... $$
    # We use a non-greedy match
    content = re.sub(r'```latex\n(.*?)\n```', r'$$\n\1\n$$', content, flags=re.DOTALL)

    # Replace inline \( ... \) with $ ... $
    content = re.sub(r'\\\((.*?)\\\)', r'$\1$', content)
    
    # Optional: replace \[ ... \] with $$ ... $$
    content = re.sub(r'\\\[(.*?)\\\]', r'$$\n\1\n$$', content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Formatting fixed!")
