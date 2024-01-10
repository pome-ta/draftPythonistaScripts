from pathlib import Path
import json

json_path = Path('./data.json')
#json_obj = json.loads(json_path.read_bytes())
json_obj = json.loads(json_path.read_text(encoding='utf-8'))
print(json.dumps(json_obj, ensure_ascii=False, indent=2))
