
mon = int(input("Enter the Sales for Monday :"))
tue = int(input("Enter the Sales for Tuesday :"))
wed = int(input("Enter the Sales for Wednesday :"))
thur = int(input("Enter the Sales for Thursday :"))
fri = int(input("Enter the Sales for Friday :"))
sat = int(input("Enter the Sales for Saturday :"))
sun = int(input("Enter the Sales for Sunday :"))
weekly_sales={
    "mon":mon,
    "tue":tue,
    "WEdnesday":wed,
    "Thursday":thur,
    "Friday":fri,
    "Saturday":sat,
    "Sunday":sun
}
total_sales = sum(weekly_sales.values())
print(total_sales)
