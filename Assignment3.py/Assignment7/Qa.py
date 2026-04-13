# Pattern (a) — Diamond of stars

n = 5

# upper part
for i in range(n):
    print(" "*(n-i-1) + "*", end="")
    if i > 0:
        print(" "*(2*i-1) + "*")
    else:
        print()

# lower part
for i in range(n-2, -1, -1):
    print(" "*(n-i-1) + "*", end="")
    if i > 0:
        print(" "*(2*i-1) + "*")
    else:
        print()
