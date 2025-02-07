# 📊 Auto-Graded Physics Quiz

def run_quiz():
    score = 0
    total_questions = 5

    questions = [
        {
            "question": "1️⃣ Which of the following is a scalar quantity?",
            "options": ["a) Force", "b) Velocity", "c) Acceleration", "d) Energy"],
            "answer": "d"
        },
        {
            "question": "2️⃣ What is the value of gravitational acceleration on Earth?",
            "options": ["a) 8.9 m/s²", "b) 9.8 m/s²", "c) 10.5 m/s²", "d) 12.3 m/s²"],
            "answer": "b"
        },
        {
            "question": "3️⃣ The unit of electric charge is:",
            "options": ["a) Joule", "b) Tesla", "c) Coulomb", "d) Watt"],
            "answer": "c"
        },
        {
            "question": "4️⃣ Which law states that the current through a conductor is directly proportional to the voltage across it?",
            "options": ["a) Faraday’s Law", "b) Ohm’s Law", "c) Newton’s Law", "d) Ampere’s Law"],
            "answer": "b"
        },
        {
            "question": "5️⃣ In quantum mechanics, what does the Heisenberg Uncertainty Principle relate to?",
            "options": ["a) Energy and Mass", "b) Force and Distance", "c) Position and Momentum", "d) Charge and Current"],
            "answer": "c"
        }
    ]

    print("📊 **Physics MCQ Quiz**\n")

    # Quiz loop
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").strip().lower()

        if answer == q["answer"]:
            score += 1
        print("\n")

    # Save the results
    with open("results.txt", "w") as file:
        file.write(f"Your score: {score}/{total_questions}\n")
        file.write(f"Percentage: {(score / total_questions) * 100:.2f}%\n")

    print(f"✅ Quiz Completed! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    run_quiz()
