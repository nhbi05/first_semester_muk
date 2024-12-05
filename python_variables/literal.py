choice = input("What will you eat? (Chicken or None)\n")
if choice == "Chicken":
    choice = 'Chicken'
else:
    choice = None
if choice:
    print(r"Didn't know you love chicken!!")
else:
    print('You have no choice')
    print(choice)
    print(type(choice))
choice = 'None'
print(choice)
print(type(choice))