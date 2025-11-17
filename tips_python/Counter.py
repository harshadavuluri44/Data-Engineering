from collections import Counter

var = 'abcdefbefzkrembax'

d = Counter(var)
print(d)
print(type(d))
print(d.get('e',0))


# Counter takes an iterable as input like string, list, tuple etc