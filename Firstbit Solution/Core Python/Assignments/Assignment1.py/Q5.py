# Write a program to enter P, T, R and calculate Compound Interest

# p = 10
# t = 20
# r = 30
# n = 4

# CI = (p/1+r/n)**(n*t-p)

# print(CI)

# Taking input form users

P = int(input("Enter the principle amount: "))
T = int(input("Enter the time period: "))
R = int(input("Enter the rate of intrest: "))
N = int(input("Enter the tiome of years: "))


CI = (P/1+R/N)**(N*T-P)

print("Compound Intresrt =" ,CI)



