# 5. Check if number present in list and count occurrences

lst = [10, 20, 30, 20, 40, 20]

num = int(input("Enter number: "))

found = False
count = 0

for i in lst:
    if i == num:
        found = True
        count += 1

if found:
    print(num, "is present", count, "times")
else:
    print(num, "is NOT present")
