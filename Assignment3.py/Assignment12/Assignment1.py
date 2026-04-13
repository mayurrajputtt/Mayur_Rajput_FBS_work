# 1. Replace all ‘a’ with $

s = "banana"
result = ""

for ch in s:
    if ch == 'a':
        result += '$'
    else:
        result += ch

print(result)