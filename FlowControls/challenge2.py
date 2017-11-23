
ipAddress = input("Please enter ip adrress in format *.*.*.* : ")

# numOfSegments = 0
number1 = ''

count = 0
# print(type(number1))
#
# for Char in range(0, len(ipAddress)):
#     if ipAddress[Char] == '.':
#         # numOfSegments += 1
#         if number1 != '':
#             count += 1
#         number = 0
#         continue
#     number1 = number1 + ipAddress[Char]

for char in ipAddress:

    if char == '.':
        if number1 != '':
            count += 1
    number1 = ''
    number1 = number1 + char
else:
    count += 1

print(count)
