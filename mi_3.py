
def isPowerOfThree(n):
    if n == 0:
        print(False)
    if n == 1.0:
        print(True)
        return True
    if n%3 == 0:
        n = n/3
        #print(n)
        isPowerOfThree(n)
    if n%3 != 0:
        return False
print(isPowerOfThree(27))