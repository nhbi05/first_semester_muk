weekly_sales = []
days = ["Monday","Tuesday","Wednesay", ]
for day in days:
    sale = int(input(f"Enter the sale for {day} :"))
    weekly_sales.append(sale)
total_sales = sum(weekly_sales)
ave= total_sales/7
minimum=min(weekly_sales)
maximum=max(weekly_sales)
print(total_sales)
print(ave)
print(minimum)
print(maximum)

"""basic_salary = int(input("Enter basic salary: "))
tax = int(input("Enter tax: "))
insurance = int(input("Enter insurance: "))
transport_allowance = int(input("Enter transport: "))
food_allowance = int(input("Enter food: "))
net_salary = basic_salary - (tax+insurance)+(transport_allowance+food_allowance)
print(net_salary) 



bal = int(input)
if bal >10000:
    interest = 0.02*bal
    #print(f"Your interest is {interest}")
elif 1000<=bal <=10000:
    interest = 0.015*bal
    #print(f"Your interest is {interest}")
else:
    interest = 0.01*bal
    #print(f"Your intersest is {interest}")
print(f"Your interest is {interest}")
     """