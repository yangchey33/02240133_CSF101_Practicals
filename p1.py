import random

number = random.randint(0,50)
guess = 0

print("Lets play a number guessing game")
print("Guess a number between 0 and 50")

while guess != number:

    guess = int(input("Enter Your Guess: "))

    if (guess < number):
        print("Guess lower")
    elif (guess > number):
        print("Guess higher")
    else:
        print("You won")

print("Game over")