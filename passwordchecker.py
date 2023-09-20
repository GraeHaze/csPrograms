
print("INSTRUCTIONS!!!")
print("--> yor password must contain minimum of 8 characters")
print("--> yor password must contain only '1,0,_' these mentioned characters")

password=input("enter the desiered password:")

flag = True
for character in password:
    if character =="0" or character =="1" or character=="_":
        continue
    else:
        flag=False
        break



if len(password)>=8 and flag == True:
    print("password correct")
else:
    print("password Incorrect")