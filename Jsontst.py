import json

with open("user.json", "r", encoding="utf-8") as f:
    a = json.load(f)

print(a)
