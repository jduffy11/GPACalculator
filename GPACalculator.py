grades = []
cHours = []

#Collects the data of Class names and Grades in Letter Form
def calculate(cHours):
    total= 0
    k = 0
    while k < len(cHours):
        for score in grades:
            if( score >= 90 and score <= 100):
                total = total + (4.0 * cHours[k])
                k += 1
            elif( score >= 80 and score <= 89):
                total = total + (3.0 * cHours[k])
                k += 1
            elif( score >= 70 and score <= 79):
                total = total + (2.0 * cHours[k])
                k += 1
            elif( score >= 60 and score <= 69):
                total = total + (1.0 * cHours[k])
                k += 1
            elif( score < 60):
                total = total + 0.0
                k += 1

    gpa = total / numCredits
    print()
    print("GPA:", gpa)

numClasses = int(input("Enter the number of classes you are taking: "))
numCredits = int(input("Enter the number of credit hours you are taking: "))

i = 0
cHoursTotal = 0
while i < numClasses:
    grade = int(input("Enter Your Grade For Each Class : "))
    grades.append(grade)
    cHour = int(input("Enter how many credit hours this class is worth: "))
    cHours.append(cHour)
    cHoursTotal = cHoursTotal + cHours[i]
    i += 1
calculate(cHours)


