import numpy as np
from givens import *

def main():
    i = 1
    j = 0

    matrix = givens_template(1, 0, 4, 9, 9)

    print(matrix)



    matrix = np.loadtxt('driver_data\givens.txt', usecols=range(4))

    print(matrix)

    i = int(input())
    j = int(input())
    

    matrix = givens_m_n_hessenberg(matrix, i, j)

    print(matrix)

if __name__ == '__main__':
    main()