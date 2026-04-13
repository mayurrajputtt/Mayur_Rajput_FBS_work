# Pattern (h) — Two number pyramids

n = 5

for i in range(1, n+1):
    # left side
    for j in range(1, i+1):
        print(j, end=" ")

    # spaces
    print(" "*(2*(n-i)), end=" ")

    # right side
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()
