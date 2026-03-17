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

score = 0  # Counter for correct answers

# Loop through each question
for i, q in enumerate(test_bank, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    for option in q["options"]:
        print(option)

    # Ask the user for an answer
    answer = input("Your answer (A/B/C): ").upper().strip()

    # Check if the answer is correct
    if answer == q["correct_answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['correct_answer']}")

# Function to print final results
def final_result(score, total_questions):
    percentage = (score / total_questions) * 100
    print(f"\n🎉 Quiz finished! Your final score: {score}/{total_questions} ({percentage:.2f}%)")
    if percentage >= 50:
        print("🎊 Congratulations! You passed the quiz.")
    else:
        print("😔 Sorry! You failed the quiz.")

# Call the final result function
final_result(score, len(test_bank))