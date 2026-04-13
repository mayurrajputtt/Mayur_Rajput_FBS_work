# 5. Count vowels

s = "education"
vowels = "aeiou"
count = 0

for ch in s:
    if ch.lower() in vowels:
        count += 1

print(count)