# m = 3
# n = 2
# #排列组合组合问题
# def uniquePaths(m, n):
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
import numpy  as np    
def corpFlightBookings(bookings, n):
    target = np.zeros(n)
    for i in bookings:
        target[i[0]- 1:i[1]] += i[2]
    c = list(target)
    return list(map(int,c))
            



print(corpFlightBookings(bookings,n))