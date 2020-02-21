import numpy as np

# # utf8
# import numpy as np
# import matplotlib.pyplot as plt
# x1 = np.linspace(0.5,10,100)
# x2 = np.linspace(-10,0.5,100)
# y1 = 0.5*x2
# y2 = 0.5 - 0.5*x1
# x3 = [0.5 for i in range(100)]
# y3 = np.linspace(0.25,15,100)
# plt.plot(x2,y1)
# plt.plot(x1,y2)
# plt.plot(x3,y3)
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.title("决策区域分布图")
# plt.text(-6, 7.5, "W1", size = 15, alpha = 0.8,color = "red")
# plt.text(5, 7.5, "W2", size = 15, alpha = 0.8,color = "blue")
# plt.text(0, -3, "W3", size = 15, alpha = 0.8,color = "black")
# plt.xlabel("x1")
# plt.ylabel("x2")
# plt.show()
# target_str = ""
# def countSegments(s):
#     c = list(s)
#     count = 0
#     add = 0
#     for i in range(len(c)):
#         if c[i] != ' ':
#             if i + 1 == len(c):
#                 add = 1
#             if i+1 < len(c):
#                 if c[i+1] == ' ':
#                     add = 1
#             count += add
#             add = 0
#     return count



# print(countSegments(target_str))
# nums = [56,12,14,23,12,14,45,79]
# def fastsort(nums):
#     if len(nums) <= 1:
#         return nums
#     index = nums[0]
#     left = [i for i in nums if i < index]
#     right = [i for i in nums if i > index]
#     middle = [i for i in nums if i  == index]
#     return fastsort(left) + middle + fastsort(right)
# print(fastsort(nums))

a = np.mat([[3,15,0],[0,33*(5**0.5)/5,-48*(5**0.5)/5],[0,-6*(5**0.5)/5,111*(5**0.5)/5]])
b =np.mat([[1,0,0],[0,11*(5**0.5)/25,-2*(5**0.5)/25],[0,2*(5**0.5)/25,11*(5**0.5)/25]])
print(b*a)