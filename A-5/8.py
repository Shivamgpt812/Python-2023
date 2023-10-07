# Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots
a=int(input("Enter a number = "))
b=int(input("Enter a number = "))
c=int(input("Enter a number = "))
d=b**-4*a*c
if d>0:
    print("real & distinct roots")
elif d==0:
    print("real & equal roots")
else:
    print("imaginary roots")