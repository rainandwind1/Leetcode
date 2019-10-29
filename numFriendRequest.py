ages = [16,17,18]
#3
# def numFriendRequests(ages):
#     count = 0
#     def judge_bridge(B,A):
#         if B <= 0.5*A + 7 or B > A or (B > 100 and  A < 100):
#             return 0
#         else:
#             return 1
#     for i in range(len(ages) - 1):
#         for j in range(i + 1,len(ages)):
#             count += judge_bridge(ages[i],ages[j]) + judge_bridge(ages[j],ages[i])
#             print(ages[i],ages[j],judge_bridge(ages[i],ages[j]),[j],[i],judge_bridge(ages[j],ages[i]))
#     return count

def numFriendRequests(ages):
    result = 0
    target = [0 for i in range(121)]
    for i in range(len(ages)):    
        target[ages[i]] += 1
    for i in range(len(ages)):
        index1 = int(ages[i] * 0.5 + 7)
        result += sum(target[index1 : ages[i]]) - 1
    return result
print(numFriendRequests(ages))