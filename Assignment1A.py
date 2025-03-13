import random

def rock_paper_scissors():
    """Plays a game of Rock, Paper, Scissors."""

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    rock_paper_scissors()