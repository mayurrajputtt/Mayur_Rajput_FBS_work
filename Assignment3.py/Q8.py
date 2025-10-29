# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# # failed. (Something like captcha)
import random

correct_userid = "1234"
correct_password = "Mayur@123"

userid = input("Enter the userid: ")
password = input("Enter the password: ")

if(correct_userid == userid) and  (correct_password == password):
    print("Login credentials verified! ")

    captcha = random.randint(1000, 9999)
    print("your varifacition code is", captcha)

    user_captcha = int(input("Enter the varification code: "))

    if(user_captcha == captcha):
        print("Successfully login.")

    else:
        print("Invalid varification code.")

else:   
    print("Invalid Userid or Password")






