
num = [1,2,4,16,32,64,75,78]

i = 0

while i < len(num):
    if(num[i]%2 == 0):
        print("This is even " +str(num[i]))
    else:
        print("This is an odd " +str(num[i]))
    i = i+1