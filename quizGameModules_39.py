# -------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key, value in questions.items():
        print("---------------------------")
        print(key)
        for option in options[question_num - 1]:
            print(option)
        guess = input("Enter the answer (A,B,C,D): ").upper()
        guesses.append(guess)  # for the first parameter value is fine too

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


# -------------------
def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("Results")
    print("---------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses / len(questions))*100)
    print("Your score is: " + str(score))

# -------------------
def play_again():
    response = None
    while response == "" or (response != "yes" and response != "no"):
        response = input("Do you want to play again? (yes/no): ").lower()
    if response == "yes":
        return True
    elif response == "no":
        return False


# -------------------

questions = {"How many elements are in the periodic table?: ": "C",
             "Which animal lays the largest eggs?: ": "D",
             "What is the most abundant gas in Earth's atmosphere?: ": "A",
             "How many bones are in the human body?: ": "A",
             "Which planet in the solar system is the hottest?: ": "B"}

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
