import numpy as np
np.set_printoptions(suppress=True)#取消科学计数法

#QR(Grem_schmidt)
def Grem_schmidt(A):
    Q = np.zeros_like(A);
    cnt = 0;
    for a in A.T:
        u = np.copy(a);
        for i in range(0,cnt):
            u -= np.dot(np.dot(Q[:,i].T,a),Q[:,i])
        e = u / np.linalg.norm(u)
        Q[:,cnt] = e
        cnt += 1
    R= np.dot(Q.T,A)
    return (Q,R)
