#You are given an array containing n distinct numbers taken from the range 0 to n. 
# Find the one number that is missing from the array.


array = [3,4,1,0]

sum=0
for x in array:
    sum+=x

n = len(array)
actualSum = n*(n+1)//2

missing_number = actualSum-sum

print(missing_number)


