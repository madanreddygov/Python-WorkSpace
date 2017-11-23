import random

highest = 10
randomNumber = random.randint(1, highest)

guess = int(input(print("Please enter your guess number between {} and {}. "
                        "Enter 0 to quit".format(1, highest))))
if guess != randomNumber:
    while guess != randomNumber:
        if guess == 0:
            print("Game Over !")
            break
        elif guess < randomNumber:
            print("Please choose higher number: ")
            guess = int(input())
        elif guess > randomNumber:
            print("Please choose lower number: ")
            guess = int(input())
    else:
        print("You guessed it")
else:
    print("You guessed it in the first attempt")


