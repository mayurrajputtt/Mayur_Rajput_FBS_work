# 2. Check Armstrong number using recursion

def power(n, p):
    if p == 0:
        return 1
    return n * power(n, p-1)

def armstrong_sum(num, digits):
    if num == 0:
        return 0
    return power(num % 10, digits) + armstrong_sum(num // 10, digits)

num = int(input("Enter number: "))
digits = len(str(num))

if armstrong_sum(num, digits) == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")
