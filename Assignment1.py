import random

number = random.randint(1,20)
guess = 0

while guess != number:

    guess = int(input("Enter Guess: "))

    if (guess < number):
        print("Guess lower")
    elif (guess > number):
        print("Guess higher")
    else:
        print("You won")
