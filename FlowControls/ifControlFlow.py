# name = input("Please enter your name: ")
# age = int(input("{}, Please enter your age: ".format(name)))

# Verify you are eligible to vote
# if age >= 18:
#     print("{0}, you are old enough to vote".format(name))
# else:
#     print("%s, please come back after %d years "%(name, 18-age))
#
# x=None
# if x:
#     print("Iam true")

name = input("Please enter your name: ")
age = input("%s, Please enter your age: "%(name))

if not(int(age)<18):
    print("You are old enough to vote")
else:
    print("please come back after {} years".format(18-int(age)))