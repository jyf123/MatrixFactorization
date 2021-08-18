import numpy as np
np.set_printoptions(suppress=True)#取消科学计数法

#PA=LU分解函数
def LU(A):
    n = len(A)
    P = np.eye(n)
    L = np.zeros([n,n])

    for base in range(n-1):
        maxi = base+1
        for i in range(base+1,n):
            L[i,base] = A[i,base]/A[base,base]
            A[i] = A[i]-L[i,base]*A[base]
            basew = (A[base+1]!=0).argmax(axis=0)
            w = (A[i]!=0).argmax(axis=0)
            if((basew!=(base+1)) and (w==(base+1))):
                maxi = i
        #实现行的交换
        if((base+1) != maxi):
            A[[base + 1, maxi], :] = A[[maxi, base + 1], :]
            L[[base + 1, maxi], :] = L[[maxi, base + 1], :]
            P[[base + 1, maxi], :] = P[[maxi, base + 1], :]
    for i in range(n):
        L[i,i] = 1
    U = np.array(A)
    return (P,L,U)
