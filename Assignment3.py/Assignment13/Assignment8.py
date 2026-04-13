# 8. Word frequency using dictionary

s = "python is easy and python is powerful"
words = s.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)