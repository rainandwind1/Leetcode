S = "---"
K = 3
# def licenseKeyFormatting(S, K):
#     c = list(S)
#     while '-' in c:
#         c.remove('-')
#     print(c)
#     count = 0
#     add_count = 0
#     l = len(c)
#     while True:
#         count += 1
#         c[len(c) - count - add_count - 1] = str(c[len(c) - count - add_count - 1]).upper() 
#         if count == l:
#             break
#         if count % K == 0:
#             c.insert(len(c) - count - add_count,'-')
#             add_count += 1
#     target = ''.join(c)
#     return target


def licenseKeyFormatting(S, K):
    target = ''
    count = 0
    for i in S[::-1]:
        if i != '-':
            l = i.upper()
            target = l + target
            count += 1
            if count % K == 0:
                l = '-'
                target = l + target
    if target:
        if target[0] == '-':
            target = target[1:]
    return target
print(licenseKeyFormatting(S,K))