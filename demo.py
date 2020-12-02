grades = []

#Collects the data of Class names and Grades in Letter Form
def calculate():
    total= 0
    for score in grades:
        if( score >= 90 and score <= 100):
            total = total + 4.0
        elif( score >= 80 and score <= 89):
            total = total + 3.0
        elif( score >= 70 and score <= 79):
            total = total + 2.0
        elif( score >= 60 and score <= 69):
            total = total + 1.0
        elif( score < 60):
            total = total + 0.0

    gpa = total / 4
    print()
    print("GPA:", gpa)

y= 0;
while (y <=3):
    grade = int(input("Enter Your Grade For Each Class : "))
    grades.append(grade)
    y = y + 1
calculate()
