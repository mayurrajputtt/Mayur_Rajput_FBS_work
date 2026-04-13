# 6. Remove duplicates from list (no inbuilt functions)

lst = [10, 20, 10, 30, 20, 40]
new = []

for i in lst:
    exists = False
    for j in new:
        if i == j:
            exists = True
            break
    if not exists:
        new.append(i)

print("List without duplicates =", new)
