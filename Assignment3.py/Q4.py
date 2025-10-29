# Write a program to input all sides of a triangle and check whether triangle is valid or
# not.

a = float(input("Enter the a side: "))
b = float(input("Enter the b side: "))
c = float(input("Enter the c side: "))

#  a b c

# Check triangle validity using Triangle Inequality Theorem

# Therom : (a + b > c)  (b + c > a) (c + a > b): 


if(a + b > c) and (b + c > a) and (c + a > b):
    print("This is the valid triangles")

else:
    print("This is not valid triangle")



