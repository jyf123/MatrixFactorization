
import numpy as np
import sys,os


# 从文件中导入数组
def load_array(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        mat = []
        for line in lines:
            line =line.strip()
            if "#" in line:
                continue
            if len(line)<1:
                continue
            line = line.split(' ')
            line = list(map(eval, line))
            mat.append(line)
        file.close()
        mat = np.array(mat, dtype=np.float64)
        m,n = mat.shape
        # if model=="LU" and m!= n-1:
        #     print("your input should be a square matrix")
        #     sys.exit()
        #     return np.array([]),0,0
        return mat, m, n

