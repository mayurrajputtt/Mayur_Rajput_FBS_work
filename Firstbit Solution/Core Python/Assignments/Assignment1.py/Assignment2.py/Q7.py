# Find the sum of three-digit number.

num = int(input("Enter the three digit num: "))

last_digit = (num % 10)

middle_digit = (num // 10) % 10

first_digit = (num // 100)

sum = (first_digit + middle_digit + last_digit)

print(sum)



