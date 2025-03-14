import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, scissors game!")

while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You loss!")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break
        else:
             print("Thanks for playing!")