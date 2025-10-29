# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter the 3 digit number: "))

last_digit = num % 10 

middle_digit = (num // 10) % 10 

first_digit = num // 100

reversed = (last_digit * 100) + (middle_digit * 10) + first_digit

# print(reversed)

if(num == reversed):
    print("It is a palindrome ")

else:
    print("It is not a palindrome ")

    