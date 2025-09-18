a=[1,7,35,90,101]
b=[4,10,21,29,98,109,343]

i=j=0
ans=[]

while i<len(a) and j<len(b):
    if a[i]<b[j]:
        ans.append(a[i])
        i+=1

    else:
        ans.append(b[j])
        j+=1

ans.extend(a[i:])
ans.extend(b[j:])

print(ans)
        