import time
import msvcrt

# ------------------ Questions ------------------

quiz = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "3. Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "4. What is the output of 5 // 2 ?",
        "options": ["A. 2", "B. 2.5", "C. 3", "D. 2.0"],
        "answer": "A"
    },
    {
        "question": "5. Which company developed Python?",
        "options": ["A. Google", "B. Microsoft", "C. Python Software Foundation", "D. None of the above"],
        "answer": "D"
    }
]

# ------------------ Timer Function ------------------

def timed_input(timeout):
    print(f"\nYou have {timeout} seconds to answer.")

    start = time.time()

    answer = ""

    while True:
        if msvcrt.kbhit():
            char = msvcrt.getche().decode().upper()

            if char == '\r':
                print()
                return answer

            answer += char

        if time.time() - start > timeout:
            print("\nTime's Up!")
            return None

# ------------------ Quiz Game ------------------

score = 0

print("=" * 40)
print("        PYTHON QUIZ GAME")
print("=" * 40)

for q in quiz:

    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user = timed_input(10)

    if user is None:
        print("No answer submitted.")
    elif user == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", q["answer"])

print("\n" + "=" * 40)
print("Quiz Finished")
print("=" * 40)

print("Your Score:", score, "/", len(quiz))

percentage = (score / len(quiz)) * 100

print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good Job!")
elif percentage >= 40:
    print("Keep Practicing!")
else:
    print("Better Luck Next Time!")