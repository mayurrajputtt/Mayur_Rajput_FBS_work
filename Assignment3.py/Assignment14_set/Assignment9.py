# 9. Unique combinations of 3 numbers with target sum

lst = [1, 2, 3, 4, 5]
target = 9
result = set()

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        for k in range(j + 1, len(lst)):
            if lst[i] + lst[j] + lst[k] == target:
                result.add((lst[i], lst[j], lst[k]))

print(result)