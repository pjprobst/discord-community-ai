import json

new_lines = []
with open("rpitt_query_2.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        obj.pop("id", None)  # remove id if it exists
        new_lines.append(json.dumps(obj, ensure_ascii=False))

with open("rpitt_query_2.jsonl", "w", encoding="utf-8") as f:
    for line in new_lines:
        f.write(line + "\n")
print("done!")
