# Given a string, find the first non-repeating character and return its index. 
# If it doesn’t exist, return -1.

string = input('Enter test case')

d = {}
n = len(string)
found = False

for i in range(n):
    if string[i] not in d.keys():
        d[string[i]]=[1,i]
    else:
        d[string[i]][0]+=1

for i in string:
    if d[i][0]==1:
        print(i,d[i][1])
        found=True
        break

if found==False:
    print('-1')