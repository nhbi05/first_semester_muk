name = input("What is your name?: \n")
print(f"Hello, {name}!")
mark =[]
for i in range (4):
    marks = int(input(f"What was your mark for course {i+1}"))
    mark.append(marks)
print(mark)
average = sum(mark)/len(mark)
print(f"Your average is {average}")
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
"""
def grading():
    student ={}
    name = input("What is the students name :\n")
    programming = int(input("Enter the mark for Programming : "))
    arch = int(input("Enter the mark for Computer Architecture: "))
    literacy = int(input("Enter the mark for Computer Literacy: "))
    communication = int(input("Enter the mark for Computer Literacy: "))
    course_units={
        'programming':programming,
        'arch':arch,
        'literacy':literacy,
        'communication':communication
    }
    student[name]= course_units
    #print(f"Student with name{name} {student[name]["arch"]}")
    average = sum(course_units.values())/len(course_units)
    print(f"Your average is {average}")
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
stds_grades=grading()
"""