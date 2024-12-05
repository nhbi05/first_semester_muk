"""fruits = ['orange', 'apple']
fruits2 = fruits
fruits3 = fruits.copy()
fruits2.append ('mango')# correct way to append is fruits2.append('mango')
print(fruits)
print(fruits2)
print(fruits3)
# for a set you use .add
this_set = {'apple', 'banana', "orange"}
this_set.remove("banana")
this_set.add("mango")
print(this_set)"""

""""""

fruits=("jackfruit", "orange", "apple", "banana", "melon", "mango") 
for i in range (len(fruits)):
    if i>4:
        break
    if i%2==1:
        print(fruits[-i])