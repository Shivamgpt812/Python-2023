# Write a python script to display the number of days in a given month number.
a=int(input("Enter The Value Of Month = "))
match a:
    case a if a in [1,3,5,7,8,10,12]:
        print("31 Days")
    case a if a in [4,6,9,11]:
        print("30 Days")
    case a if a in [2]:
        print("28 Days or 29 Days")