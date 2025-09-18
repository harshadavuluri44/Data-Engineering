nums = [1, 2, 4, 5, 6]  # n = 6

n = len(nums)+1

sum = n*(n+1)//2

for x in nums:
    sum = sum - x

print(sum)