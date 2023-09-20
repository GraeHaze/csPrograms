num = int(input("Enter the number"))
max = num
min = num
for i in range(1,5 ):
    num = int(input("Enter the number"))
    if num > max:
        max = num
    elif num < min:
        min = num
print("maximum Value : ",max,"\nMininum Value : ",min)