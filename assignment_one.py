#get student details
student_name= input("Enter your name: \n")
student_number= input("Enter your student number: \n")
#getting the last digits of the student no
num1 = int(student_number[-1])
num2 =  int(student_number[-2])
#initialising lists to store marks,coursecodes and credit units 
marks =[]
credits =[]
course_codes =[]

#loop for collecting course codes, marks and credit units for four courses
for i in range (4):
    course_code = (input(f"Enter the  course code for course {i+1} : \n"))
    course_codes.append(course_code)
    mark = int(input(f"Enter your marks for course {i+1} (0-100): \n"))
    marks.append(mark)
    credit_unit = int(input(f"Enter credit units for course {i+1}: \n"))
    credits.append(credit_unit)
    
#assigning grades points to the marks
def calc_grade_point(marks):
    if  0<= marks <=100:
        if marks >= 90:
            return 5
        elif marks >= 80:
            return 4
        elif marks >= 70:
            return 3
        elif marks >= 60:
            return 2
        elif marks >= 50:
            return 1 
        else :
            return 0
    else :
            print ("Invalid marks .Please enter a value between 0 and 100")
#computing the CGPA
def calc_cgpa (marks,credits):
    total_points = 0
    credit_units = 0

    for i in range(len(marks)):
        grade_points = calc_grade_point(marks[i])
        total_points += grade_points * credits[i]
        credit_units += credits[i]
    cgpa = total_points / credit_units
    return cgpa


cgpa = calc_cgpa(marks, credits)
print(f"Your CGPA is :{cgpa :.2f}")
print("-----------------------------------------------")

#basic calculator
def basic_calculator(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2 
    multiplication = num1* num2
    if num1 != 0:
        division = num1/num2
    else:
        division = "Undefined"

    print (f"Addition: \n {num1} + {num2} = {addition}")
    print (f"Subtraction:\n {num1} - {num2} = {subtraction}")
    print (f"Multipication: \n {num1} * {num2} = {multiplication}")
    print (f"Division: \n {num1} / {num2} = {division :.5f}")
basic_calculator(num1, num2)