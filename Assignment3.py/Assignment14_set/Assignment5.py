# 5. Longest common prefix using set

strings = ["flower", "flow", "flight"]

prefix = ""
for i in range(len(strings[0])):
    ch = strings[0][i]
    if all(s[i] == ch for s in strings):
        prefix += ch
    else:
        break

print(prefix)