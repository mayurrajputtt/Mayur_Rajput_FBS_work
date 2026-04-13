# 10. Remove even numbers from list

lst = [1, 2, 3, 4, 5, 6]

result = []

for x in lst:
    if x % 2 != 0:
        result.append(x)

print(result)
