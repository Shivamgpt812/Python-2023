# Write a python script to print first N even natural numbers
i=1
n=int(input("Enter the Number"))*2

while i<=n:
    if i%2==0:
        print(i)
    i+=1