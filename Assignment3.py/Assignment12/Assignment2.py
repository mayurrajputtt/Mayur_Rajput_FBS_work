# 2. Remove nth index character

s = "python"
n = 2
result = ""

for i in range(len(s)):
    if i != n:
        result += s[i]

print(result)