# 8. Group anagrams

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for w in words:
    key = "".join(sorted(w))
    if key in groups:
        groups[key].append(w)
    else:
        groups[key] = [w]

print(list(groups.values()))
