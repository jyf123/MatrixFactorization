# 矩阵分析与应用大作业
### 环境
* python3.7.5
### 文件结构
```
MatrixFactorization
|____ data                          # 样例文件夹，其中的example.txt包含了用于测试的所有矩阵
|____ venv                          # 环境文件夹
|____ main.py                       # 运行的主函数
|____ LU.py                         # LU分解过程脚本
|____ Grem_schmidt.py               # Schmidt过程函数脚本
|____ Housholder_reduction.py       # Housholder约简函数脚本
|____ Givens_reduction.py           # Givens约简函数脚本
|____ URV.py                        # URV分解函数脚本
|____ LoadData.py                   # 加载矩阵数据脚本

```
### 参数含义
运行python脚本
>python main.py -h

将给出提示
```
-h, --help            show this help message and exit
--model {LU,QR,HR,GR,URV}
                        5 choices in ['LU','QR','HR','GR','URV'], LU->LU
                        Factorization, QR->Schmidt Procedure, HR->Housholder
                        Reduction, GR->Givens Reduction, URV->URV
                        Factorization!
--input INPUT         input example file path.
```
运行时分解过程的选项有五种，各选项代表的含义为：
  - `--model=LU`  : LU分解
  - `--model=QR`  : Gram-Schmidt
  - `--model=HR`  : Housholder约简
  - `--model=GR`  : Givens约简 
  - `--model=URV` : URV分解
### 运行实例和结果
>python main --model=LU --input=data/example.txt
#### 输出
```
P=[[1. 0. 0. 0.]
 [0. 0. 0. 1.]
 [0. 0. 1. 0.]
 [0. 1. 0. 0.]]
L=[[ 1.    0.    0.    0.  ]
 [-3.    1.    0.    0.  ]
 [ 2.   -0.2   1.    0.  ]
 [ 4.    0.    3.75  1.  ]]
U=[[ 1.    2.   -3.    4.  ]
 [ 0.    5.   -8.    8.  ]
 [ 0.    0.    6.4  -5.4 ]
 [ 0.    0.    0.   -3.75]]
```

>python main --model=QR --input=data/example.txt
#### 输出
```
Q=[[ 0.   -0.8  -0.6 ]
 [ 0.6   0.48 -0.64]
 [ 0.8  -0.36  0.48]]
R=[[ 5. 25. -4.]
 [ 0. 25. 10.]
 [ 0. -0. 10.]]
```

>python main --model=HR --input=data/example.txt
#### 输出
```
Q=[[ 0.   -0.8  -0.6 ]
 [ 0.6   0.48 -0.64]
 [ 0.8  -0.36  0.48]]
R=[[ 5. 25.  0.]
 [ 0. 25. 10.]
 [ 0.  0. 10.]]
```

>python main --model=GR --input=data/example.txt
#### 输出
```
Q=[[ 0.   -0.8  -0.6 ]
 [ 0.6   0.48 -0.64]
 [ 0.8  -0.36  0.48]]
R=[[ 5. 25. -4.]
 [ 0. 25. 10.]
 [-0. -0. 10.]]
```

>python main --model=URV --input=data/example.txt
#### 输出
```
U=[[-0.66666667 -0.66666667  0.33333333]
 [ 0.33333333 -0.66666667 -0.66666667]
 [-0.66666667  0.33333333 -0.66666667]]
R=[[9. 0. 0. 0.]
 [0. 3. 0. 0.]
 [0. 0. 0. 0.]]
V=[[ 0.66666667  0.          0.66666667  0.33333333]
 [ 0.          1.         -0.         -0.        ]
 [ 0.66666667 -0.         -0.33333333 -0.66666667]
 [ 0.33333333 -0.         -0.66666667  0.66666667]]

```
