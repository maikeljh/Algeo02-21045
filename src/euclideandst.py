import numpy as np

def euclideandst(vektor1, vektor2):
    """
    Function to calculate euclidean distance between two vectors

    Args:
        vektor1 (array): vector 1 (same size)
        vektor2 (array): vector 2 (same size)

    Returns:
        sum (float): the euclidean distance
    """
    sum = 0
    for i in range(len(vektor1)):
        sum += ((vektor1[i] - vektor2[i]) * (vektor1[i] - vektor2[i]))
    sum = np.sqrt(sum)
    return sum

def shortestDst(vektor, matriksVektor):
    """
    Function to determine shortest euclidean distance

    Args:
        vektor (array): the vector weight of test image
        matriksVektor (matrix): the list of vector weight of training images

    Returns:
        idx (int): the index of the closest image
        cachemin (float) : the shortest euclidean distance
    """
    cachemin = euclideandst(vektor, matriksVektor[0])
    idx = 0
    for i in range(1, len(matriksVektor)):
        sum = euclideandst(vektor, matriksVektor[i])
        if sum < cachemin:
            cachemin = sum
            idx = i
    return idx, cachemin