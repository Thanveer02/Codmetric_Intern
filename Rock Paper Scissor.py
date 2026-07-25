import random
choices = ["rock", "paper", "scissor"]
while True:
    mychoice = input("Enter your choice: ")
    computer_choice = random.choice(choices)
    if mychoice == computer_choice:
        print("Draw!")
    elif mychoice == "rock" and computer_choice == "scissor":
        print(f"your choice {mychoice} and computer choice {computer_choice},You win!")
    elif mychoice == "paper" and computer_choice == "rock":
        print(f"your choice {mychoice} and computer choice {computer_choice},You win!")
    elif mychoice == "scissor" and computer_choice == "paper":
        print(f"your choice {mychoice} and computer choice {computer_choice},You win!")
    else:
        print(f"your choice {mychoice} and computer choice {computer_choice},You lose!")
    playagain = input("Do you want to play again? (yes/no): ")
    if playagain != "yes":
        print("Thanks for playing!")
        break
