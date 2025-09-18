a = [1, 3, 5, 7]
b = [2, 4, 6, 8,10,17]


ans = []

x = len(a)
y = len(b)

i=j=0

while i<x and j<y:
    while a[i]<b[j]:
        ans.append(a[i])
        i+=1
    while b[j]<a[i]:
        ans.append(b[j])
        j+=1

print(ans)