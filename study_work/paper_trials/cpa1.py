marks = []
course1 = int(input("what is your mark for course1?:  "))
course2 = int(input("what is your mark for course2?:  "))
course3 = int(input("what is your mark for course3?:  "))
course4 = int(input("what is your mark for course4?:  "))
marks.append(course1,course2,course3,course4)#append takes one argument only
print(marks)
average = sum(marks)/len(marks)
if average >=90:
        print(f"you passed with a grade of A+")
elif average >= 80:
        print(f"you passed with a grade of A")
elif average >= 70:
        print(f"you passed with a grade of B")
elif average >= 60:
        print(f"you passed with a grade of C")
else:
        print(f"You have failed with an F")