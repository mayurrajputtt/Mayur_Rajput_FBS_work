# Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!

n = int(input("Enter the value of n: "))

sum_fact = 0 

fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum_fact = sum_fact + fact

print("Sum of series is:", sum_fact)

