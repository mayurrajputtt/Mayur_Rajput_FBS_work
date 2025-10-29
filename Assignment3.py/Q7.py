# Write a program to check if user has entered correct userid and password.

correct_userid = "1234"
correct_password = "Mayur@123"

userid = (input("Enter the userid: "))
password = (input("Enter the password: "))

if(userid == correct_userid) and (password == correct_password):
    print("Successfully login")

else:
    print("Invalid password or userid.")




