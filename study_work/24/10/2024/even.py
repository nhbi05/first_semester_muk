maximum = int(input("Enter the maximum number: "))
total = 0
for num in range(1, maximum+1):
    if num %2==0:
        total = total +num
        print(total)
print("The sum of even numbers from 1 to {0} ={1} ".format(num , total))
