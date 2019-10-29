deck1 = [1,2,3,4,4,3,2,1]
deck2 = [1,1,1,2,2,2,3,3]
deck3 = [1]
def hasGroupsSizeX(deck):
    target = {}
    for i in deck:
        target[i] = target.get(i,0) + 1
    ct = [i for i in target.values()]
    if len(ct) == 1:
        if ct[0] >= 2:
            return True
        else:
            return False
    t = []
    ct.sort()
    index = 1
    for i in range(1,int(ct[0]**0.5) + 1):
        if ct[0]%i == 0:
            m = int(ct[0] / i)
            t.append(i)
            if m not in t:
                t.append(m)
    def resolve(index,tp):
        if index == len(ct):
            return tp
        mv = []
        for i in range(1,ct[index]):
            if ct[index]%i ==0:
                if int(ct[index]/i) in tp:
                    mv.append(int(ct[index]/i))
        if mv == []:
            return False
        return resolve(index + 1,mv)

    while True:
        result = resolve(index,t)
        if result == False:
            return False
        r = max(result)
        if r >= 2:
            return True
print(hasGroupsSizeX(deck2))