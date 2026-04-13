# Pattern (d) — Number pattern (1, then reverse)

n = 5

for i in range(1, n+1):
    print(" "*(n-i), end="")

    # ascending numbers
    for j in range(i, i+i):
        print(j, end=" ")

    # descending numbers
    for j in range(i+i-2, i-1, -1):
        print(j, end=" ")

    print()
