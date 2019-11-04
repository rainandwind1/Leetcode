nums = [1,1,1]
k = 2
import math
import bisect
def numSubarrayProductLessThanK(nums, k):
    # count_len = 1
    # target = 1
    # result = 0
    # add_r = 0
    # l = len(nums)
    # while True:
    #     for i in range(l - count_len + 1):
    #         for j in range(count_len):
    #             target *= nums[i + j]
    #         if target < k:
    #             add_r += 1
    #         target = 1
    #     result += add_r
    #     if add_r == 0:
    #         return result
    #     count_len += 1
    #     if count_len == l + 1:
    #         return result
    #     add_r = 0
    if k == 0:
        return 0
    k = math.log(k)

    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + math.log(x))

    ans = 0
    for i,x in enumerate(prefix):
        j = bisect.bisect(prefix,x+k - 1e-9,i+1)
        ans += j - i - 1
    return ans


print(numSubarrayProductLessThanK(nums,k))