# 8. Print 1 to 100 (Snakes and Ladder pattern)

num = 1

for row in range(10):
    line = []
    for col in range(10):
        line.append(num)
        num += 1

    if row % 2 == 1:
        line.reverse()

    print(line)


