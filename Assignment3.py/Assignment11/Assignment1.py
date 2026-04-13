# 1. Even and Odd elements into two lists

lst = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for x in lst:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Even list:", even)
print("Odd list:", odd)
