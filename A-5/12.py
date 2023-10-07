# Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
a=complex(input("Enter a number = "))
if a.imag>a.real:
    print("imaginary is greater")
else :
    print("real is greater")