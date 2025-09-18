nums = [4, 5, 9, 4, 2, 9, 1, 5]

s = set()
r = []

for x in nums:
    if x not in s:
        s.add(x)
        r.append(x)

print(r)