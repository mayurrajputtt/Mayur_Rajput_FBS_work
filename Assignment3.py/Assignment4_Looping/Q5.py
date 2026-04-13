# WAP to print Fibonacci series upto n.

num = int(input("Enter the number: "))

a = -1
b = 1

for i in range(1, num):
    c = a + b
    print(c, end=" ")
    a = b
    b = c