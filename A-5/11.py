# Write a python script to take the month value in numeric format and display the number of days in it.
a=int(input("Enter The Value Of Month = "))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12 :
    print("31 Days")
elif a==2 :
    print("28or29 days")
else:
    print("30 Days")