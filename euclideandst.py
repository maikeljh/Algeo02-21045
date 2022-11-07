import numpy as np

def euclideandst(vektor1, vektor2):
#vektor 1 sama 2 ukurannya sama kan ya
    sum = 0
    for i in range(len(vektor1)):
        sum += pow(vektor1[i] - vektor2[i], 2)
    sum = np.sqrt(sum)
    return sum

def shortestDst(vektor, matriksVektor):
#matriksVektor si jumlah kolomnya sama kek vektor 2 kan ya
    cachemin = max()
    for i in range(len(matriksVektor)):
        sum = 0
        sum = euclideandst(vektor, matriksVektor[i])
        if sum < cachemin:
            cachemin = sum
    return cachemin