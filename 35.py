nums = [1,3,5,6]
target = 5 
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] < target:
            continue
        return i
    return len(nums)

print(searchInsert(nums,target))