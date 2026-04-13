# 15. Find larger string (no built-in)


a = "hello"
b = "education"

la = lb = 0

for _ in a:
    la += 1
for _ in b:
    lb += 1

if la > lb:
    print(a)
else:
    print(b)