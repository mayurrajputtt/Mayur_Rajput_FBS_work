# 14. Count occurrences of each word

s = "python is easy and python is powerful"
words = s.split()

for w in words:
    print(w, ":", words.count(w))