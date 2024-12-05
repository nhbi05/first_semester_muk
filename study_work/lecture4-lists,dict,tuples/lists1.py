"""Without using the in and not in operators, write of program will 
print ask a user for some input to input some lake and check 
whether that input is part of the list"""

lakes = ['Nabugabo', 'Birinzi', 'Kyoga', 'Wamala', 'Edward']

user = input("Enter the lake name: ")
for lake in lakes:
    if lake == user:
        print("lake is in")
        break
    else:
        print("not there")

#correct code
"""
lakes = ['Nabugabo', 'Birinzi', 'Kyoga', 'Wamala', 'Edward']

user = input("Enter the lake name: ")
found = False
for lake in lakes:
    if lake == user:
        found=True
        break
if found:
    print(f"{user} is found")
else:
    print(f"{user} is not found")
"""

    
