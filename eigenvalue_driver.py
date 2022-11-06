import numpy as np
from eigenvalue import eigenvalue_array

def main():
    matrix = np.loadtxt('driver_data\eigenvalue.txt', usecols=range(5))

    print(matrix)

    result = eigenvalue_array(matrix)

    print(result)

if __name__ == '__main__':
    main()

