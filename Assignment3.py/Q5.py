# Write a program to check whether the triangle is equilateral, isosceles or scalene
# triangle.

a = int(input("Enter the a side: "))
b = int(input("Enter the b side: "))
c = int(input("Enter the c side: "))

if(a + b > c) and (b + c > a) and (c + a > b):
    print("If this is valid triangle.")

# If all three sides are equal → Equilateral Triangle
    if(a == b == c):
        print("This is an Equilateral triangle.")

# If any two sides are equal → Isosceles Triangle
    elif(a == b) or (b == c) or (c == a):
         print("This is an Isosceles tringle")

# If all three sides are different → Scalene Triangle
    else:
        print("this is an scalane triangle")

else:
    print("This is not a triangle")






