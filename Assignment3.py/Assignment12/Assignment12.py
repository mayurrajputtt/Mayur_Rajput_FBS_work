# 12. Count lowercase letters


s = "PyThOn"
count = 0

for ch in s:
    if ch >= 'a' and ch <= 'z':
        count += 1

print(count)