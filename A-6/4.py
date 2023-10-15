# Write a program which takes user’s age and display the category of person. Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 - Experienced, Age above or equal 60 - Senior Citizen.
age=int(input("Enter Your Age\t"))
print(age)
match age:
    case age if age<=10:
        print("KID")
    case age if 10<age<=20:
        print("Teen")
    case age if 20<age<=40:
        print("Young")
    case age if 40<age<=60:
        print("Experienced")
    case age if 60<age:
        print("Senior Citizen")