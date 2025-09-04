import json

def flatten_text(items):
    if isinstance(items, list):
        return " ".join([str(i) for i in items])
    return str(items)

with open("train2.jsonl", "r", encoding="utf-8") as f, open("train_prepared2.jsonl", "w", encoding="utf-8") as out:
    for line in f:
        data = json.loads(line)
        text = data["question"].strip() + " " + flatten_text(data["context"])
        answer = flatten_text(data["answers"])
        out.write(json.dumps({"text": text, "answers": answer}, ensure_ascii=False) + "\n")
