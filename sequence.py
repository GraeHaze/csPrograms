flag=True
n=int(input("enter the number :"))
for i in range(5,n,5):
    if flag==True:
        print(i*-1)
        flag=False
    else:
        print(i)
        flag=True