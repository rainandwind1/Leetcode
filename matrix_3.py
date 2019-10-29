import numpy as np
# A = np.matrix('1,1,1,1,1,1,1,1,1,1,1;-5,-4,-3,-2,-1,0,1,2,3,4,5')
# b = np.matrix('2,7,9,12,13,14,14,13,10,8,4')
# A = A.T
# b = b.T
# x = (A.T*A).I*A.T*b

# a0 = x[0,0]
# b0 = x[1,0]
# sum_er = 0
# for i in range(11):
#     sum_er += (A[i,1]*b0 + a0 - b[i,0])**2
#     print(A[i,1],b[i,0]) 
# print(sum_er)

A = np.matrix('1,1,1,1,1,1,1,1,1,1,1;-5,-4,-3,-2,-1,0,1,2,3,4,5;25,16,9,4,1,0,1,4,9,16,25')
b = np.matrix('2,7,9,12,13,14,14,13,10,8,4')
A = A.T
b = b.T
x = (A.T*A).I*A.T*b
print(x)
a0 = x[0,0]
b0 = x[1,0]
c0 = x[2,0]
sum_er = 0
for i in range(11):
    sum_er += (A[i,2]*c0 + A[i,1]*b0 + a0 - b[i,0])**2
    print(A[i,1],b[i,0]) 
print(sum_er)