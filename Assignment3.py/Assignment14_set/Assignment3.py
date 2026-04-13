# 3. Unique words and frequency (using set)

lst = ["apple", "banana", "apple", "orange", "banana"]
unique = set(lst)

for word in unique:
    print(word, ":", lst.count(word))