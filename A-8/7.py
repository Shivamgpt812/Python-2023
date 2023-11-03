# Write a python script to print first N even natural numbers in reverse order
i=1
n=int(input("Enter the Number"))*2

while n>=i:
    if n%2==0:
        print(n)
    n-=1