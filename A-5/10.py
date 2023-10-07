# Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
a=int(input("Enter a number = "))
b=int(input("Enter a number = "))
c=int(input("Enter a number = "))
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater")
else:
    print(c,"is greater")