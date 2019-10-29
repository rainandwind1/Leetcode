nums = [2, 2, 3, 3, 3, 4]
def deleteAndEarn(nums):
    old = 0
    new = 0
    l = max(nums)
    c = {}
    for i in nums:
        c[i] = c.get(i,0) + 1
    target = [0 for i in range(l + 1)]
    for key in c:
        target[key] = c[key]
    for i in range(len(target)):                                         
        old,new = new,max(old + i*target[i],new)
    return new


print(deleteAndEarn(nums))