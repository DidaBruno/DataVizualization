import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

filtered = [
    { "Strani jezik": item.get("Strani jezik"), }
    for item in data
]

with open("filtered.json", "w", encoding="utf-8") as f:
    json.dump(filtered, f, ensure_ascii=False, indent=2)