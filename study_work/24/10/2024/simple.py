def calculate_simple_interest(principal,rate,time):
    interest = (principal*rate*time)/100
    return interest
#Get user input for principal,rate and time
principal_amount = float(input("Enter princal amount: "))
annual_rate = float(input("Enter the annual rate: "))
time_period = float(input("Enter the time in years: "))
#Calculate simple intrest
simple_interest = calculate_simple_interest(principal_amount,annual_rate,time_period)
print(f"The simple interest is : {simple_interest}")