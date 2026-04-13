# Pattern (f) — Mixed number pattern

n = 5

for i in range(1, n+1):
    print(i, end=" ")
    if i == 1:
        for j in range(2, 6):
            print(j, end=" ")
    elif i < 5:
        print(" "*(2*(5-i)-1), end="")
        print(5)
    else:
        print()
