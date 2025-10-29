# Write a program to input any alphabet and check whether it is vowel or consonant.

alpha = input("Enter the alphabet: ") # You not take in this int beacuse it it not an number

alpha = alpha.lower() # Convert to lowercase to handle both uppercase and lowercase letters

if alpha in ('a','e','i','o','u'):
    print(" It is an vowel")
else:
    print("It is an Constant")
    










