import json
import os

DATA_DIR = "data"
QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.json")
LEADERBOARD_FILE = os.path.join(DATA_DIR, "leaderboard.json")
os.makedirs(DATA_DIR, exist_ok=True)

# Load questions
with open(QUESTIONS_FILE, "r") as f:
    questions = json.load(f)

# Load leaderboard
if os.path.exists(LEADERBOARD_FILE):
    with open(LEADERBOARD_FILE, "r") as f:
        leaderboard = json.load(f)
else:
    leaderboard = []

score = 0
name = input("Enter your name: ")

print("\n🧠 Quiz Started!\n")

for q in questions:
    print(q["question"])
    for idx, opt in enumerate(q["options"], start=1):
        print(f"{idx}. {opt}")

    choice = input("Your answer (1-4): ")
    if q["options"][int(choice) - 1] == q["answer"]:
        score += 1
        print("✅ Correct!\n")
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}\n")

print(f"🎯 Final Score: {score}/{len(questions)}")

leaderboard.append({"name": name, "score": score})

# Save leaderboard
with open(LEADERBOARD_FILE, "w") as f:
    json.dump(leaderboard, f, indent=4)

# Display leaderboard
print("\n🏆 Leaderboard")
leaderboard_sorted = sorted(leaderboard, key=lambda x: x["score"], reverse=True)

for idx, entry in enumerate(leaderboard_sorted[:5], start=1):
    print(f"{idx}. {entry['name']} - {entry['score']}")

print("\n✅ Quiz Completed!")
