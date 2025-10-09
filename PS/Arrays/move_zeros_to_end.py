# Given an integer array, move all the zeroes to the end while keeping the order of 
# non-zero elements the same.


nums = [1, 0, 0, 3, 12]

i = 0  # position to place the next non-zero
for j in range(len(nums)):
    if nums[j] != 0:
        x=nums[j]
        nums[i]=x
        nums[j]=0
        i+=1

print(nums)


