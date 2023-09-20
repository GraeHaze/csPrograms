"""
----*
---***
--*****
-*******
*********
"""

height = int(input("Enter the height of the Triangel: "))
spaces = height-1
for i in range(0,height):
    stars = 2*i+1
    print(" "*spaces,end="")
    print("*"*stars)
    spaces-=1

