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