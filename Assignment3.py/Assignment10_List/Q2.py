# 2. Program to find maximum and minimum element (no inbuilt function)

lst = [10, 50, 30, 5, 90]

maxi = lst[0]
mini = lst[0]

for i in lst:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

print("Maximum =", maxi)
print("Minimum =", mini)
