# 4. Second largest number using Bubble Sort

lst = [10, 20, 5, 40, 30]
n = len(lst)

for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Second largest:", lst[-2])
