# quiz.py

# List of questions in dictionary format
test_bank = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kaduna"],
        "correct_answer": "B"
    },
    {
        "question": "Who is the GOAT?",
        "options": ["A. Ronaldo", "B. Pele", "C. Messi"],
        "correct_answer": "C"
    }
]

score = 0  # Keep track of correct answers

for i, item in enumerate(test_bank, start=1):
    print(f"\nQuestion {i}: {item['question']}")
    for option in item["options"]:
        print(option)

    answer = input("Your answer (A/B/C): ").upper().strip()
    if answer == item["correct_answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {item['correct_answer']}")

print(f"\n🎉 Quiz finished! Your score: {score}/{len(test_bank)}")

test_bank = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kaduna"],
        "correct_answer": "B"
    },
    {
        "question": "What is 3 + 3?",
        "options": ["A. 1", "B. 6", "C. 4"],
        "correct_answer": "B"
    },
    {
        "question": "Who is the GOAT?",
        "options": ["A. Ronaldo", "B. Pele", "C. Messi"],
        "correct_answer": "C"
    }
]
score = 0

for q in quiz:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    answer = input("Your answer (A/B/C): ").strip().upper()
    
    if answer == q["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['correct_answer']}.")

def final_result(score, total_questions):
    percentage = (score / total_questions) * 100
    print(f"\nYour final score: {score}/{total_questions} ({percentage:.2f}%)")
    if percentage >= 50:
        print("Congratulations! You passed the quiz.")
    else:
        print("Sorry! You failed the quiz.")

final_result(score, len(quiz))