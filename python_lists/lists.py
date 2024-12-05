number = []
numbers =[[5,6,7,8], [6,7,8,9], [5,6,6,6] ,[2,1,2,3]]
print(numbers[3][1])# to access the items in the list we index them for examples list 3, index 1
#going from the right to left we use negatives, then the other way 0
print(len(numbers))#get the length of the lisst

#slicing
list2 =[1,2,3,4,5,6,7,8,9]
list3 = list2[0:9:2]
list4=list2[1::2]
print(list2[-2::-2])
#print(list2[0::])
print(list3)
print(list4)
fruits = ["grapes", "jackfruit", "apples", "mango","banana"]
print(fruits[1:3])
print(fruits[:3])
print(fruits[1:4:2])
print(fruits[-2::-2])

list2[3] = 'cow'
print (list2)
list2[2:6]=[5,6,7,8]
print (list2)
list2[-2::-2]=[5,6,7,8]
print (list2)
