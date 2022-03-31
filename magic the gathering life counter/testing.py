
#when rolling a dice (numbers 1-6)
import random

def rollDice(min, max):
    while True:
        print("Roling dice...")
        number = random.randint(min,max)
        print(f"Your number: {number}")
        choice = input("Do you want to roll the dice again? (y/n)")
        if choice.lower() == 'n':
            break

rollDice(1,6)