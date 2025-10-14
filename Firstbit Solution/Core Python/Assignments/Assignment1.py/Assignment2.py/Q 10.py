# Write a program to reverse three-digit number.

num = int(input("Enter the value: "))

last_digit = (num % 10)

middle_digit = (num // 10) %10

first_digit = num // 100

reversed_num = (last_digit * 100) + (middle_digit * 10) + first_digit

print(reversed_num)
