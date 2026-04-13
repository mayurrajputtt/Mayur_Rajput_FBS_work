# 6. Replace space with hyphen

s = "hello world python"
result = ""

for ch in s:
    if ch == " ":
        result += "-"
    else:
        result += ch

print(result)
