def item_book():
    items = []
    no_of_items = int(input("Enter the number of items sold: "))
    for i in range(no_of_items):
        item_name = input('Enter the name of the item: ')
        items.append(item_name)
    print(items)
    sales = []
    def sales_calc():
        for item in items:
            quantity = int(input(f"Enter the quantity of the {item} sold out: "))
            cost = int(input(f"Enter the cost of the {item} sold: "))
            item_sales = quantity*cost
            sales.append(item_sales)
    sales_calc()
    print(sales)
    return sales

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
daily_sales_per_week = []
for day in days:
    print(f" Recording sales for {day} ")
    daily_sales = item_book()
    daily_sales_per_week.append(daily_sales)
    print(f"Total sales for {day}: {sum(daily_sales)}")
    print(daily_sales_per_week)