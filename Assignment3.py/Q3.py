# Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int(input("Enter the a angle: "))
b = int(input("Enter the b angle: "))
c = int(input("Enter the c angle: "))

sum = a+b+c

if(sum == 180):
    print("The triangle is valid")

else:
    print("The triangle is not valid")

    