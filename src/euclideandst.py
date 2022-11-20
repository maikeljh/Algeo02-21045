import numpy as np

def euclideandst(vektor1, vektor2):
#vektor 1 sama 2 ukurannya sama kan ya
    sum = 0
    for i in range(len(vektor1)):
        sum += ((vektor1[i] - vektor2[i]) * (vektor1[i] - vektor2[i]))
    sum = np.sqrt(sum)
    return sum

def shortestDst(vektor, matriksVektor):
#matriksVektor si jumlah kolomnya sama kek vektor 2 kan ya
    cachemin = euclideandst(vektor, matriksVektor[0])
    idx = 0
    for i in range(1, len(matriksVektor)):
        sum = euclideandst(vektor, matriksVektor[i])
        if sum < cachemin:
            cachemin = sum
            idx = i
    return idx, cachemin