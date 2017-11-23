
#  File creation and input

Cities = ["Kansas City", "Dallas", "New York", "Houston", "St.Louis"]

with open("cities.txt", "w") as cities_file:
    for city in Cities:
        print(city.strip('\n\r'), file=cities_file)




with open("cities.txt", "r") as cities_file:
    for city in cities_file:
        print(city.strip('\n'))