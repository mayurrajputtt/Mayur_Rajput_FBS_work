# 10. Display larger string (without built-in)

s1 = "python"
s2 = "programming"

c1 = c2 = 0

for _ in s1:
    c1 += 1
for _ in s2:
    c2 += 1

if c1 > c2:
    print(s1)
else:
    print(s2)
