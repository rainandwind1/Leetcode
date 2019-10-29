A = 'abcde'
B = 'bcdea'
def rotateString(A, B):
    A_ = list(A)
    B_ = list(B)
    for i in range(len(A)):
        target = A_[0]
        A_.remove(A_[0])
        A_.append(target)
        if A_ == B_:
            return True
    return False

print(rotateString(A,B))