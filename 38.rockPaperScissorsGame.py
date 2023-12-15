import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print("Computer: " + computer)
        print("Player: " + player)
        print("Tie!")

    elif player == "rock" and computer == "scissors":
        print("Computer: " + computer)
        print("Player: " + player)
        print("Player win!")

    elif player == "paper" and computer == "rock":
        print("Computer: " + computer)
        print("Player: " + player)
        print("Player win!")

    elif player == "scissors" and computer == "paper":
        print("Computer: " + computer)
        print("Player: " + player)
        print("Player win!")

    else:
        print("Computer: " + computer)
        print("Player: " + player)
        print("Computer win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again == "yes":
        pass
    elif play_again == "no":
        break
print("bye!")
