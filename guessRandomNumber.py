import random

low = int(input("Select the lowest number you want to be able to guess"))
high = int(input("Select the highest number you want to be able to guess"))

randomNum = random.randint(low,high)
guess = .2
while(guess != randomNum):
    guess = int(input("Guess the random number"))
else:
    print("Congrats you guessed the random number")