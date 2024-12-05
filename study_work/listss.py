#progrm that will prompt a user for 10 integers and print out the sum of positive and negati
"""inetgers=[]
total_positive =0
total_negative =0
for i in range(10):
    no = int(input(f"Enter a no {i+1}: "))
    inetgers.append(no)
    
    if no <0:
        total_negative+=no
    else:
        total_positive+=no
print(total_negative)
print(total_positive)"""

lakes =["Nabugabo","Birinzi","Kyoga","Wamala","Edward"]
lake = input("What lake are you looking for?: ")
for _ in lakes :
    if lake in lakes :
        print(f"The {lake} is found")
    else:
        print(f"The {lake} is not found")