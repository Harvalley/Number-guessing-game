import random

print ("Welcome to the Number guessing Game!")
print ("I am thinking of a number between 1 and 100.")
print()

secret = random.randint(1, 100)
attemots = 0

while True:
    guess = int(input("Enter your guess: "))
    attemots += 1

    if guess < secret:
        print("Too low, try again.")
    elif guess > secret:
        print("Too high, try again.")
    else:
        print(f"Congratulations! You guessed the number in {attemots} attempts.")
        break   