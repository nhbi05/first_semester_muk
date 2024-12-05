even_count = 0
odd_count = 0
numbers = "8,3,10,16,13,12,8,8,3,4"
numbers =numbers.split(",")
for num in numbers : 
    if num < 0 : #since none of the numbers is less than zero the final answer is 0 for both
        if num %2 ==0:
            even_count+= 1
        else:
            odd_count+=1
print ("Count of even numbers", even_count)
print ("Count of odd numbers", odd_count)