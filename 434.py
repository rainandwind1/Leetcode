target_str = ""
def countSegments(s):
    c = list(s)
    count = 0
    add = 0
    for i in range(len(c)):
        if c[i] != ' ':
            if i + 1 == len(c):
                add = 1
            if i+1 < len(c):
                if c[i+1] == ' ':
                    add = 1
            count += add
            add = 0
    return count



print(countSegments(target_str))