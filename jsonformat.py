import json
import glob
import re

files = glob.glob("exported_data/*.json")

with open("clean_qna_with_context.jsonl", "w", encoding="utf-8") as out_file:
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            question = data.get("channel", {}).get("name", "").strip()
            messages = data.get("messages", [])
            if not question or not messages:
                continue

            question_author_id = messages[0].get("author", {}).get("id")

            answers = []
            context = []

            for msg in messages:
                author = msg.get("author", {})
                content = msg.get("content", "").strip()
                if not content:
                    continue

                if author.get("id") == question_author_id:
                    context.append(content)
                elif not author.get("isBot", False):
                    answers.append(content)

            if not answers:
                continue  

            json.dump({
                "question": question,
                "context": context,
                "answers": answers
            }, out_file, ensure_ascii=False)
            out_file.write("\n")

print("Done! Generated clean_qna_with_context.jsonl with answers and question-author context.")
