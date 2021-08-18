import numpy as np
np.set_printoptions(suppress=True)#取消科学计数法

#Householder reduction
def Householder_reduction(A):
    """Householder变换"""
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    cnt = 0
    for cnt in range(c - 1):
        x = R[cnt:, cnt]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        u = x - e
        v = u / np.linalg.norm(u)
        Q_cnt = np.identity(r)
        Q_cnt[cnt:, cnt:] -= 2.0 * np.outer(v, v)
        R = np.dot(Q_cnt, R)  # R=H(n-1)*...*H(2)*H(1)*A
        Q = np.dot(Q, Q_cnt)  # Q=H(n-1)*...*H(2)*H(1)  H为自逆矩阵
    (r1,c1) = np.shape(R)
    for i in range(r1):
        for j in range(c1):
            if R[i][j]-0<=0.000000000000000001:
                R[i][j]=0

    return (Q,R)