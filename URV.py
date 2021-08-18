import numpy as np
np.set_printoptions(suppress=True)#取消科学计数法
from Householder_reduction import Householder_reduction

# #URV
def URV(A):
    (r1,c1) = np.shape(A)
    (Q1,R1) = Householder_reduction(A);
    U = Q1
    (r2,c2) = np.shape(R1)
    i=0
    for i in range(r2):
        cnt=0
        for j in range(c2):
            if((R1[i,j]-0)<=0.0000000000001):
                cnt += 1
        if(cnt==c2):
            break
    B = R1[0:i]
    # print("B={}".format(B))
    (Q2,R2) = Householder_reduction(B.T)
    V = Q2
    # print("Q2={}".format(Q2))
    # print("R2={}".format(R2))
    (r3,c3) = np.shape(R2)
    m=0
    for m in range(r3):
        cnt = 0
        for n in range(c3):
            if ((R2[m, n] - 0) <= 0.0000000000001):
                cnt += 1
        if (cnt == c3):
            break
    t = R2[0:m]
   # print("t={}".format(t))
    (r4,c4) = np.shape(t)
    R = np.zeros_like(A)
    R[0:r4,0:c4] = t.T
    return (U,R,V)
