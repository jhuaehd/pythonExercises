age = int(input("Enter your age \n"))

if age >= 18:
    voter = input("Enter Municipaplity \n")
    if voter == "Limasawa":
        print("Voter from Limasawa")
    else:
        print("You are not a voter here")
else:
    print("YOu are not a voter")
print("Thank you for using the program......")
