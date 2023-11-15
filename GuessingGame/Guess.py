# A number guessing game.
import random


def guess_the_number():
    # Generate a random number
    secret_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.")

    attempts = 0

    while True:
        # Get User's guess
        user_guess = int(input("Take a guess: "))
        attempts += 1

        # Check the guess
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low try again!")
        else:
            print("Too high")


# Run the game

guess_the_number()
