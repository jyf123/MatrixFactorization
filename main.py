import numpy as np
np.set_printoptions(suppress=True)#取消科学计数法
import os
from LoadData import load_array
from LU import LU
from Householder_reduction import Householder_reduction
from Grem_schmidt import Grem_schmidt
from Givens_reduction import Givens_reduction
from URV import URV
import argparse
import sys
#参数
op = argparse.ArgumentParser(description='Five Factorization Methods')
op.add_argument("--model",type=str,choices=['LU','QR','HR','GR','URV'],default="LU",
                help="5 choices in ['LU','QR','HR','GR','URV'], LU->LU Factorization, QR->Schmidt Procedure, HR->Housholder Reduction, GR->Givens Reduction, URV->URV Factorization!")
op.add_argument("--input", type=str, default="data/example.txt",
                help="input example file path.")

args = op.parse_args()


# 计算矩阵的秩
def rank_of_matrix(mat, m, n):
    # 使用部分消元法进行初等行变换
    mat = mat.copy()
    row = col = 0
    while row < m - 1 and col < n:
        curr_col = np.abs(mat[row:, col])
        max_item = np.max(curr_col)
        # print(curr_col, max_item)
        if np.all(curr_col == 0):
            col += 1
            continue
        if curr_col[0] != max_item:  # 行交换
            max_row_idx = np.where(curr_col == max_item)[0][0] + row
            helper = mat[max_row_idx].copy()
            mat[max_row_idx] = mat[row]
            mat[row] = helper
        # print_array(mat, m, n)
        # print()

        for i in range(row + 1, m):
            if np.all(mat[i] == 0):
                break
            factor = mat[i, col] / mat[row, col]
            value = (-1 * factor * mat[row, col:])
            mat[i, col:] += value
        col += 1
        row += 1
        # print_array(mat,m,n)
        # print()

    zero_rows = 0
    for i in mat[::-1]:
        if np.all(i == 0):
            zero_rows += 1
            continue
        break
    mat_rank = min(m, n, m - zero_rows)
    # print(m,n,zero_rows,mat_rank)
    return mat_rank

if __name__ == "__main__":
    path = os.getcwd()
    input_file = path+'/'+args.input
    A,m,n = load_array(input_file)
    if A.size ==0:
        print("input Error!")
        sys.exit()

    if(args.model=="LU"):
        if m != n:
            print("your input should be a square matrix")
            sys.exit()
        (P,L,U)=LU(A)
        print('P={}'.format(P))
        print('L={}'.format(L))
        print('U={}'.format(U))
    if(args.model=='QR'):
        mat_rank = rank_of_matrix(A,m,n)
        if mat_rank<n:
            print("Error!\nThe matrix with linearly dependent columns Can Not be uniquely factored as A=QR!\n\n")
            sys.exit()
        (Q,R)=Grem_schmidt(A)
        print('Q={}'.format(Q))
        print('R={}'.format(R))
    if(args.model=='HR'):
        (Q,R)=Householder_reduction(A)
        print('Q={}'.format(Q))
        print('R={}'.format(R))
    if(args.model=='GR'):
        (Q,R)=Givens_reduction(A)
        print('Q={}'.format(Q))
        print('R={}'.format(R))
    if(args.model=='URV'):
        (U,R,V)=URV(A)
        print('U={}'.format(U))
        print('R={}'.format(R))
        print('V={}'.format(V))
