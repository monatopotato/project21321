import random
import sys


num = random.randint(0,9)
while True:
    choice = int(input("Pick a number between 0-9: "))
    if num == choice:
        print("You picked the right choice")
        sys.exit()

    elif num > choice:
        print("You guess was too low: Guess a number higher than",choice)

    elif num < choice:
        print("You guess was too high: Guess a number lower than",choice)

