# #488  废物
# import queue
# beginWord = "hot"
# endWord = "dog"
# wordList =["hot","dot","dog"]#,"lot","log","cog"]
# def ladderLength(beginWord, endWord, wordList):
#     mp = []
#     number_layer = 0
#     layer_memory = 1
#     check = []
#     q = queue.Queue()
#     begin = list(beginWord)
#     end = list(endWord)
#     layer_count = 1
#     def judge_discri(target,mu):
#         count = 0
#         for i in range(len(target)):
#             if target[i] != mu[i]:
#                 count += 1
#             if count > 1:
#                 return None,False
#         if count == 1:
#             return mu,True
#         if count == 0:
#             return None,False
#     q.put(end)
#     while not q.empty():
#         if layer_memory == 0:
#             layer_memory = number_layer
#             number_layer = 0
#             layer_count += 1
#         if layer_memory > 0:
#             layer_memory -= 1 
#         c = q.get()
#         for i in wordList:
#             mu = list(i)
#             print(c,mu,layer_count)
#             result,bool_result = judge_discri(c,mu)
#             if bool_result == True:
#                 q.put(mu)
#                 check.append(i)
#                 if layer_memory >= 0:
#                     number_layer += 1
#                 p,bool_result_ = judge_discri(result,begin)
#                 if bool_result_:
#                     return layer_count + 2
#         mp.append(number_layer)
#         for j in check:
#             wordList.remove(j)
#         print(wordList,check)
#         check = []
#         if len(wordList) == 0:
#             return 0
#     return 0

    

#488  废物
import queue
beginWord = "hot"
endWord = "dog"
wordList =["hot","dot","dog"]#,"lot","log","cog"]
def ladderLength(beginWord, endWord, wordList):
    check = []
    q = queue.Queue()
    begin = list(beginWord)
    end = list(endWord)
    layer_count = 1
    def judge_discri(target,mu):
        count = 0
        for i in range(len(target)):
            if target[i] != mu[i]:
                count += 1
            if count > 1:
                return None,False
        if count == 1:
            return mu,True
        if count == 0:
            return None,False
    q.put([end,1])
    while not q.empty():
        [c,layer_count] = q.get()
        for i in wordList:
            mu = list(i)
            print(c,mu,layer_count)
            result,bool_result = judge_discri(c,mu)
            if bool_result == True:
                q.put([mu,layer_count + 1])
                check.append(i)
                p,bool_result_ = judge_discri(result,begin)
                if bool_result_:
                    return layer_count + 2
        for j in check:
            wordList.remove(j)
        print(wordList,check)
        check = []
        if len(wordList) == 0:
            return 0
    return 0






print(ladderLength(beginWord, endWord, wordList))