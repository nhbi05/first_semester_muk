def stds():
    students ={}
    n = int(input("How many students are in the class? :\n"))
    for _ in range (n):
        name = input("What is the students' name? ")
        std_no = input ("What is the student no")
        marks =[]
        for _ in range(4):
            mark = input("What is the students mark?")
            marks.append(mark)
            students[name]= {'reg_no': std_no , 'total_marks': marks}
            print(students)
