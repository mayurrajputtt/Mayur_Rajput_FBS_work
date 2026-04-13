# 10. Reverse a number using recursion (another method)

def reverse_number(n):
    if len(n) == 1:
        return n
    return reverse_number(n[1:]) + n[0]

num = input("Enter number: ")
print("Reversed =", reverse_number(num))
