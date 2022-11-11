import numpy as np

def euclideandst(vektor1, vektor2):
#vektor 1 sama 2 ukurannya sama kan ya
    sum = 0
    for i in range(len(vektor1)):
<<<<<<< HEAD
        sum += (vektor1[i]-vektor2[i])+(vektor1[i]-vektor2[i])
=======
        sum += ((vektor1[i] - vektor2[i]) * (vektor1[i] - vektor2[i]))
>>>>>>> 5ea40425385089f17ebfe4a2f3fa875df12f15dc
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