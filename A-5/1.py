# 1. Write a python script to check whether a given number is positive or non-positive

a=int(input("Enter a number = "))
if a>=1:
    print("Positive Number")
elif a==0:
    print("Non Positive")

#or

# a=int(input("Enter a number = "))
# b=("Positive Number" if a>=1 else "Non Positive" )
# print(b)