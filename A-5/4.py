# Write a python script to print greater between two numbers. Print number only once
# even if the numbers are the same.
a=int(input("Enter a number = "))
b=int(input("Enter a number = "))
if a>b :
    print(a,"is greater")
elif b>a :
    print(b,"is greater")
elif a==b :
    print("equal")