# 7. Remove a given key

d = {'a': 10, 'b': 20, 'c': 30}
key = 'b'

if key in d:
    del d[key]

print(d)