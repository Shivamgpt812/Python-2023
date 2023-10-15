# Write a menu driven program to perform following operations - Addition, Subtraction,Multiplication, Division
print('Press 1. for addition')
print('Press 2. for subtraction')
print('Press 3. for multiplication')
print('Press 4. for division')

x=int(input("Enter your choice"))
a=int(input("Enter 1st number = "))
b=int(input("Enter 2nd number = "))

match x:
    case 1 :
        e=a+b
        print(e)
    case 2 :
        f=a-b
        print(f)
    case 3 :
        h=a*b
        print(h)
    case 4 :
        i=a//b
        print(i)
        


