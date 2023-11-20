# Dice roll simulation

import random


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


# Simulate rolling the two dice 5 times

for _ in range(1):
    result = roll_dice()
    print(f"The dice rolled: {result}")

    # Check for numbers 2 , 3 , 12
    if result in [2, 3 , 12]:
        print(f"You Crapped Out! {result}")

    # Check for numbers 7 or 11
    if result in [7, 11]:
        print(f"You win the",f"You rolled {result}")
