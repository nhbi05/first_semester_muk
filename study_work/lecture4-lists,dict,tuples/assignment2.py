students = {}
n = int(input("How many students are in the class? :\n"))
for _ in range(n):
    name = input("What is the students name?\n")
    std_no = input("What is the student number?\n")
    marks = []
    for i in range(4):
        mark = int(input(f"What is the student mark for subject {i+1}: "))
        marks.append(mark)
        students[name] = {'reg_no': std_no, 'total_marks': marks}
    print(students)

student_averages={}
def average(name):
    for name ,data in students.items():

        marks =data['total_marks']
        ave = sum(marks)/len(marks)
        student_averages[name] = {"Average", ave}
        print(student_averages)
average(name)
"""
def min_max():
    max_student = max(student_averages, key=student_averages.get)
    min_student = min(student_averages , key=student_averages.get)
    print(f'The best student is {max_student} with an average of {student_averages[max_student][]}')
    print(f'The worst student is {min_student} with an average of {student_averages[min_student][]}')
average(name)
min_max()
"""
def delete():
    item_to_delete = input("Input name to delete :")
    if item_to_delete in students:
        del students[item_to_delete]
        print(f"{item_to_delete} has been deleted")
        print(students)
    else:
        print(f"{item_to_delete} not found")
delete()

def edit():
    to_edit = input("Enter name of student whose marks you want to edit: ")
    if to_edit in students:
        student_data = students[to_edit]
        marks = student_data['total_marks']
        print(f"Current marks for {to_edit}: {marks}")

        subject_number = int(input("Enter the subject number to edit (1-4): ")) -1
        if 0 <= subject_number < len(marks):
            new_mark =int(input(f"Enter the new mark for subject {subject_number +1}: "))
            marks[subject_number] = new_mark
            print(f"Updated marks for {to_edit}: {marks}")
            #For editing avg
            student_averages [to_edit]= sum(marks)/len(marks)
            print(f"New average for {to_edit} is {student_averages[to_edit]}")
        else:
            print("Invalid subject number")

    else:
        print(f"Student {to_edit} not found")
edit()



