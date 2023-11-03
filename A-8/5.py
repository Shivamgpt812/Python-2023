# Write a python script to print first N odd natural numbers in reverse order
i=1
n=int(input("Enter the odd Number"))*2

while n>=i:
    if n%2!=0:    
        print(n)
    n-=1

   