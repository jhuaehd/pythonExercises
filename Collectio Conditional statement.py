#
# salad=["Macaroni","Fruits","Milk","Cream"]
#
# if "Macaroni" in salad and "Fruits" in salad and "Milk" in salad or "Cream" in salad:
#     print("Salad is delicious")
# else:
#     print("Ingredient lacking")

firstGrade = float(input("Enter first grade \n"))
secondGrade = float(input("Enter second grade \n"))
thirdGrade = float(input("Enter third grade \n"))
average = float((firstGrade+secondGrade+thirdGrade)/3).__round__(2)

print(average)
if 51 <= average <= 74:
    print("You failed")
elif 75 <= average <= 89:
    print("You passed")
elif 90 <= average <= 94:
    print("With Honors")
elif 95 <= average <= 97:
    print("With High Honors")
elif 98 <= average <= 100:
    print("With Highest Honor")
else:
    print("Invalid Grade")

print("\nThank you for using the program")
