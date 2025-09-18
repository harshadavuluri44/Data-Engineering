nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

n = len(nums)
ans=[]

for i in range(0,n-k+1):
    ans.append(max(nums[i:i+k]))
print(ans)