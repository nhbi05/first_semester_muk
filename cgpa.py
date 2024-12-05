def calc_cgpa():
    total_points = 0
    grades = 0
    scores =[]
    credits = []
    for x in range (4):
        course= input ("Enter course code:")
        score = int(input(f"Please enter the score for course {x+1} : "))
        credit_unit = int(input(f"Please enter the credit units for course {x+1} : "))
        scores.append(score)
        credits.append(credit_unit)
        print("--------------------------------------------------")

        total_points += credit_unit * 5
        if  0<= score <=100:
            if score >= 90:
                return 5
            elif score >= 80:
                return 4
            elif score >= 70:
                return 3
            elif score >= 60:
                return 2
            elif score >= 50:
                return 1 
            else :
                return 0
        else :
                print ("Invalid score .Please enter a value between 0 and 100")
        grades += credit_unit * score
        
    cgpa = float((grades/ total_points  )*5)
    print ("Your CGPA is : "+ str(cgpa))
calc_cgpa()
    

    