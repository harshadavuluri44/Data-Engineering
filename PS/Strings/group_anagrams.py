# Given a list of strings, group the anagrams together.

# Angaram : Two words or strings with same frequency of chars, may be in different order

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

d = {}

for x in words:
    l = sorted(x)

    x_sorted = ''.join(l)

    if x_sorted in d.keys():
        d[x_sorted].append(x)
    else:
        d[x_sorted]=[x]


print(list(d.values()))