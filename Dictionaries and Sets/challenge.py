
myText = input("Please enter some text:  ")

myList = set(myText).difference("aeiou")
print(myList)

print(sorted(myList))