# Pattern (c) — 1, 11, 121, 1331 (Pascal Triangle)

for i in range(4):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
