"""
Palandrom Examples:

wow
malayalam
lol 

steps:
    --> reverse the String
        - string slicing
    --> if the original string and reversed
        string are equal then it is a PALANDROM 
        - if statement

"""

word = input("Enter the word:")

#revering the string using string slicing
#reversed_word = word[::-1]

#reversing the stirng using while loop

# 012345
# tanish
length = len(word)-1 # 5
reversed_word = ""
while length >= 0:
    reversed_word = reversed_word + word[length]
    length-=1


if word == reversed_word:
    print("it is a palandrom")
else:
    print("it is not a palandrom")