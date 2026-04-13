# 4. Pairs whose sum equals given value

lst = [1, 2, 3, 4, 5]
target = 6

pairs = set()

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.add((lst[i], lst[j]))

print(pairs)
