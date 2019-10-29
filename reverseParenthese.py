s = "a(bcdefghijkl(mno)p)q"
print(list(s))
def reverseParentheses(s):
    left_memory = right_memory = 0
    result = list(s)
    while True:
        if '(' not in result:
            break
        for i in range(len(result)):
            if result[i] == '(':
                left_memory = i
            if result[i] == ')':  
                right_memory = i 
                target = result[left_memory + 1:i]
                target.reverse()
                result[left_memory + 1:i] = target
                break
        result.pop(left_memory)
        result.pop(right_memory - 1)
    result = "".join(result)
    return result

print(reverseParentheses(s))
##                      "tauswa"