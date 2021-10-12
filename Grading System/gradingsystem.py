import math  

def gradingStudents(grades):
    # Write your code here
    finalgrades = []

    for i in grades:
        difference = 5*math.floor(((i/5)+1))-i
        roundvalue = 5*math.floor(((i/5)+1))

        if i < 38:
            finalgrades.append(i)
        elif difference < 3:
            finalgrades.append(roundvalue)
        elif difference >= 3:
            finalgrades.append(i)
        
    return finalgrades

  
if __name__ == '__main__':
    grades_count = int(input("how many grades = "))

    grades = []
    for i in range(grades_count):
        grades_item = int(input("Marks(1-100) " + str(i+1) + " : " ))
        grades.append(grades_item)

    print("Initial Grades :", grades)
    
    print("Final Grades :", gradingStudents(grades))