a = 'amazon'
b = 'azonam'

n = len(a)
moves=0

for i in range(n):
    str = a[i+1:] + a[:i+1]
    moves+=1
    if str==b:
        print(moves)