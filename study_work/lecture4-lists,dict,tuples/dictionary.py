""" Write a Python Program to Input Information for n number of Students as Given Below:
 a. Name
 b. Registration Number
 c. Total Marks
 The user has to specify a value for n number of students. The Program Should Output the Registration 
Number and Marks of a Specified Student Given His Name

 """

def stds():
    student_stats ={}
    n = int(input("Enter the number of students\n"))
    for _ in range(n):
        name = input ("enter the student's name")
        reg_no = input ("Enter your registration number")
        total_marks = input("Enter your total marks\n")

        student_stats[name]= {'reg_no': reg_no , 'total_marks': total_marks}
        print(student_stats)
"""
    search_name = input("Enter the students name to search:")
    if search_name in student_stats:
        print(f"Registration number: {student_stats[search_name]['reg_no']}")
        print(f"total marks: {student_stats[search_name]['total_marks']}")
    else :
        print ("Student not found")"""

stds()



