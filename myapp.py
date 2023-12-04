import random


def roll_dice():
    """
    Simulate rolling two six-sided dice.

    The function generates a random number between 1 and 12 and prints the result.
    """
    result = random.randint(1, 12)
    print(f"\n------------------\nYou rolled: {result}\n------------------\n")

    print("\nIn docker since for some reason I can't type yes, if you just press the restart or play button and it "
          "will re-roll\n")


while True:
    roll_dice()

    roll_again = input("Roll the dice again? (yes/no): ").lower()

    if roll_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
