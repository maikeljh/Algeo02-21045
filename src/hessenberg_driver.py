import numpy as np
from hessenberg import hessenberg_form

def main():
    matrix = np.loadtxt('driver_data\eigenvalue.txt', usecols=range(4))

    print(matrix)

    matrix = hessenberg_form(matrix)

    print(matrix)

if __name__ == '__main__':
    main()

