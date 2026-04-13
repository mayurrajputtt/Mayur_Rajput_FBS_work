# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


userid = "Mayur123"
password = "Rajput@123"

attempts = 3

while attempts > 0:
    User = input("Enter the userid: ")
    Password = input("Enter the Password: ")

    if(userid == User and  password == Password):
        print("Login is sucessfull")
        break

    else:
        attempts -= 1
        print("Invalid Credential")

if(attempts == 0):
    print("You have use all attmpts")












