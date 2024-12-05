student_name = input("Enter your name!")
student_no = input ("Enter your student number: ")

grades =[]
credit_units = []
for i in range (4):
    marks = float(input(f"Please enter the marks for course {i+1} (0-100): "))
    credit_unit = int(input(f"Please enter the credit units for course {i+1} : "))
    #marks = float(input("Please enter your marks: "))
    if 0<= marks <= 100:
        if marks >= 90:
            grade = 5
        elif marks >= 80:
            grade = 4
        elif marks >=70:
            grade = 3
        elif marks >= 60:
            grade = 2
        elif marks >= 50:
            grade = 1
        else :
            grade = 0
        grades.append(grade)
        credit_units.append(credit_unit)
    #print ("Grade", grade)
    else:
        print ("Invalid marks .Please enter a value between 0 and 100")
    
    
if len (grades) ==4:
    for i in range(4):
        print (f"Course {i+1}  Grade:{grades[i]}")
        print (f"Course {i+1}  Credit Unit:{credit_units[i]}")
#cgpa=float()
