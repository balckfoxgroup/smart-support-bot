import json
from pathlib import Path
root = Path(r"d:\(3X-UI) + WireGuard\AI_Knowledge_Base_Multilingual")
data = json.loads((root / "_faq_en_parsed.json").read_text(encoding="utf-8"))
(root / "_faq_en_questions.txt").write_text(
    "\n".join(f"{i['id']}|{i['q']}" for i in data), encoding="utf-8"
)
print(len(data))
