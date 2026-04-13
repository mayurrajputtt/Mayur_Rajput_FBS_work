# 3. Sort list according to second element in sublist

lst = [[1, 3], [4, 1], [2, 2]]

lst.sort(key=lambda x: x[1])

print(lst)
