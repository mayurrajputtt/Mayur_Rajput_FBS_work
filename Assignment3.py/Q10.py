# Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

gender = input("Enter the gender (male/female): ")

age = int(input("Enter the age: "))

if gender == "male":
    if(age >= 21):
        print("Eligible to marry.")

    else:
        print("Not eligible to marry.")

elif gender ==  "female":
    if (age >= 18):
        print("Eligible to marry.")

    else:
        print("Not eligible to marry.")

else:
    print("Invalid gender enterd . please enterd male or female.")





    



