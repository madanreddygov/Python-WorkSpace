
menu = []

menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "spam", "bacon", "lettuce"])
menu.append(["egg", "bacon"])
menu.append(["egg", "spam"])

# print(menu)

for item in menu:
    if not "spam" in item:
        for gradient in item:
            print(gradient)