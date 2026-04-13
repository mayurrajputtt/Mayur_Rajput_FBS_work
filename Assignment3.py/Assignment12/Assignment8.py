# 8. Remove odd index characters


s = "python"
result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result += s[i]

print(result)
