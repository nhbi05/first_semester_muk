maximum = int(input("please enter maximum value:"))
total = 0

for num in range(1, maximum+1):
    if  num % 2 == 0:
        total = total + num

        print (total)

print (f"sum of even numbers from 1 to {maximum}, {total}")

"""x = [1,2,3,4,5,6,7,8,9,10]
for num in x:
    if num% 2 ==1:
        print (num)"""