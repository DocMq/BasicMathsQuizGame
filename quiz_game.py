# math_quiz_game.py

def get_quiz_data():
    questions = [
        {
            "question": "What is 5 + 3?",
            "options": ["6", "7", "8", "9"],
            "answer": 3
        },
        {
            "question": "What is 12 - 4?",
            "options": ["6", "7", "8", "9"],
            "answer": 3
        },
        {
            "question": "What is 3 x 4?",
            "options": ["10", "11", "12", "13"],
            "answer": 3
        },
        {
            "question": "What is 16 / 4?",
            "options": ["2", "3", "4", "5"],
            "answer": 3
        },
        {
            "question": "What is 7 + 6?",
            "options": ["12", "13", "14", "15"],
            "answer": 2
        },
        {
            "question": "What is 9 - 3?",
            "options": ["5", "6", "7", "8"],
            "answer": 2
        },
        {
            "question": "What is 8 x 2?",
            "options": ["14", "15", "16", "17"],
            "answer": 3
        },
        {
            "question": "What is 18 / 2?",
            "options": ["7", "8", "9", "10"],
            "answer": 3
        },
        {
            "question": "What is 10 + 4?",
            "options": ["13", "14", "15", "16"],
            "answer": 2
        },
        {
            "question": "What is 15 - 5?",
            "options": ["9", "10", "11", "12"],
            "answer": 2
        }
    ]
    return questions

def welcome_message():
    print("Welcome to the Basic Math Quiz Game!")
    print("You will be asked a series of multiple-choice questions.")
    print("Try to answer them correctly. Good luck!\n")
    input("Press Enter to start the quiz...")

def display_question(question, options):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def get_answer():
    while True:
        try:
            answer = int(input("Your answer (1/2/3/4): "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_answer(answer, correct_answer):
    return answer == correct_answer

def main():
    welcome_message()
    questions = get_quiz_data()
    score = 0
    
    for q in questions:
        display_question(q["question"], q["options"])
        answer = get_answer()
        if check_answer(answer, q["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was option {q['answer']}: {q['options'][q['answer']-1]}.\n")
    
    print(f"Your final score is: {score}/{len(questions)}")
    if score == len(questions):
        print("Congratulations! You got all the answers correct!")
    elif score > len(questions) / 2:
        print("Good job! You scored more than half.")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
