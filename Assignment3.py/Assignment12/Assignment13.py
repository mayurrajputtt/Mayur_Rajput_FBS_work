# 13. Count digits and letters

s = "abc123"
letters = digits = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)