# 1. Sum of series 1! + 2! + 3! + … + n! (using two recursive functions)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def series_sum(n):
    if n == 1:
        return 1
    return fact(n) + series_sum(n-1)

n = int(input("Enter n: "))
print("Sum =", series_sum(n))
