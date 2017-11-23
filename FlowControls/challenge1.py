name = input("Please enter your name: ")
age = int(input("{}, Please enter your age: ".format(name)))

if 18<age<31:
    print("Right age to go on for a holiday")
else:
    print("Only ages b/w 19-30 are allowed for holidays ")