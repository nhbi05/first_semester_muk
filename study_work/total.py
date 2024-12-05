def add_shipping(subtotal):
    subtotal = subtotal/5

    return subtotal 
units = 50
first_total = units* 5
total = add_shipping(first_total)
print ("Your total is ", total)
