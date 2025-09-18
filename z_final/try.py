#Count Frequency of Each Character in String

d={}
s=input("Enter a string: ")
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]+=1