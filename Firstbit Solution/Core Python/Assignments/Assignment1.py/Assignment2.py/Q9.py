# Write a program to swap two numbers without using third variable.

a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))

a = a + b

b = a - b 

a = a - b 

print(f'a is {a} b is {b}')
