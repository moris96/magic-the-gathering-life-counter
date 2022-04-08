#when rolling a dice (numbers 1-20) 20 is max dice value for magic the gathering
import random

def rollDice(min, max):
    while True:
        print("Roling dice...")
        number = random.randint(min,max)
        print(f"Your number: {number}")
        break

rollDice(1,20)