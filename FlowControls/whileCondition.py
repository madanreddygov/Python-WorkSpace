
someList = ["east", "west", "north", "south"]
chosenItem = ''

while chosenItem not in someList:
    chosenItem = input("Please enter one of the direction: ")
    if chosenItem == 'quit':
        print("Game Over!")
else:
    print("you chose: {} direction".format(chosenItem))
