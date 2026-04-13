# 6. Two numbers with maximum product

lst = [1, 10, -5, 6, -20]

lst.sort()
result = max(lst[0] * lst[1], lst[-1] * lst[-2])

print(result)