import json
import os

def process_exported_data(directory="exported_data"):
    q_and_a_data = []
    resume_advice_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                full_data = json.load(f)

            messages = full_data.get('messages', [])

            if messages:
                main_post_message = messages[0]
                main_post_content = main_post_message.get('content', '').strip()

                # All subsequent messages are replies
                replies_messages = messages[1:]
                replies_content = [msg.get('content', '').strip() for msg in replies_messages if msg.get('content')] # Filter out empty replies

                # Determine if it's a Q&A or Resume channel based on filename
                if "questions-forum" in filename.lower():
                    if main_post_content:
                        q_and_a_data.append({
                            "question": main_post_content,
                            "answers": replies_content
                        })
                elif "resume-reviews" in filename.lower():
                    if main_post_content:
                        resume_advice_data.append({
                            "resume_post": resume_post_content,
                            "feedback": feedback_content
                        })

    # Save processed data to JSON files
    with open("q_and_a.json", 'w', encoding='utf-8') as f:
        json.dump(q_and_a_data, f, indent=4, ensure_ascii=False)

    with open("resume_advice.json", 'w', encoding='utf-8') as f:
        json.dump(resume_advice_data, f, indent=4, ensure_ascii=False)

    print("--- Processed Q&A Data ---")
    for entry in q_and_a_data:
        print(f"Question: {entry['question']}")
        for i, answer in enumerate(entry['answers']):
            print(f"  Answer {i+1}: {answer}")
        print("-" * 20)

    print("\n--- Processed Resume Advice Data ---")
    for entry in resume_advice_data:
        print(f"Resume Post: {entry['resume_post']}")
        for i, advice in enumerate(entry['feedback']):
            print(f"  Feedback {i+1}: {advice}")
        print("-" * 20)

    return q_and_a_data, resume_advice_data

if __name__ == "__main__":
    q_and_a, resumes = process_exported_data()
    print(f"Total Q&A entries found: {len(q_and_a)}")
    print(f"Total Resume Advice entries found: {len(resumes)}")
