citations = [1,2,2]
def hIndex(citations):
    if citations == []:
        return 0
    citations.sort(reverse = True)
    mean = int(sum(citations)/len(citations))
    index_1 = index_2 = mean
    print("init:",index_1,"\n")
    if mean > len(citations):
        index_1 = index_2  = len(citations)
    if len(citations) == 1:
        return min(citations[0],1)
    if len(citations) <= citations[len(citations) - 1]:# and mean > 0:
        return len(citations)
    while True:
        if index_1 - 1 >= 0 and index_1 < len(citations):
            if index_1 <= citations[index_1 - 1] and index_1 >= citations[index_1]:
                return index_1
                print("return index_1\n") 
                break
        if index_2 - 1 >= 0 and index_2 < len(citations):
            if index_2 <= citations[index_2 - 1] and index_2 >= citations[index_2]:
                return index_2 
                print("return index_2\n") 
                break
        if index_1 - 1 >= 0:
            index_1 -= 1
        if index_2 + 1 <= len(citations) - 1:
            index_2 += 1

# if len(citations) - index_1 >= 0 and len(citations) - index_1 < len(citations):
#             if index_1 <= citations[len(citations) - index_1]:
#                 return index_1 
#                 break
#         if len(citations) - index_2  >= 0 and len(citations) - index_2 < len(citations):
#             if index_2 <= citations[len(citations) - index_2]:
#                 return index_2 
#                 break
            

print(hIndex(citations))