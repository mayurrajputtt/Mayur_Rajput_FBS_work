# 3. Program to find second largest element (no inbuilt function)

lst = [10, 50, 30, 90, 80]

largest = lst[0]
second = -999999

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest =", second)
