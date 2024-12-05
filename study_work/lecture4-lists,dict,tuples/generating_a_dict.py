""" write a program to generate a dictionary from keys and values provided by a user"""
keys = []
values= []
num_items = int(input("Enter the numberof key value pairs you want:\n"))
for i in range(num_items):
    key= input(f"Key please { i+1}!:")
    value = input("Value too: ")
    values.append(value)
    keys.append(key)
dict =dict(zip(keys,values))#zip basically pairs the kys to coresponding values

print(f"The dict is", dict)