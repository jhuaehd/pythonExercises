grade = float(input("Grade : "))
while grade < 50:
    print("Invalid grade!!")
    grade = float(input("Grade : "))
else:
    gradetwo = float(input("Grade two : "))
    while gradetwo < 50:
        print("Invalid grade two")
        gradetwo = float(input("Grade two : "))
    else:
        gradethree = float(input("Grade three : "))
        print(grade,gradetwo,gradethree)