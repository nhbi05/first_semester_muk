even_count =0
odd_count =0
numbers = '8,3,5,7,6,4,3,5,2'
numbers = numbers.split(",")
numbers = [int(num) for num in numbers]
for num in numbers:
    if num>0:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
print("Count of even numbers", even_count)
print("Count of odd numbers", odd_count)