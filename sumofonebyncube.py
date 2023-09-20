num = int(input("Enter the limit:"))
totalsum = 0
for i in range(1, num+1):
    totalsum = totalsum + (1/(i**3))
    print("+","1/",i**3, end=" ")
print("= ",totalsum)