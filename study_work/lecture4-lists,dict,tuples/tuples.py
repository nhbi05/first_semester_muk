"""Prompts for an integer,n, from the user.
  Prompts for n values from the user.
  Creates a tuple of n items
  Prints the tuple to the console"""
values=[]

number = int(input("no of times:"))
for i in range(number):
    value= input("Enter the value: ")
    values.append(value)

tuples = tuple(values)
print("This is a tuple",tuples)

