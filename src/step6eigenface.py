import numpy as np

def EigenFaces(eigen_vectors, k, difference):
    """
    Compute the eigenfaces from eigen vectors and difference

    Args:
        eigen_vectors (array): list of eigen vectors
        k (integer): the amount of eigen vector
        difference (matrix): the difference of matrix face and mean face

    Returns:
        listOfEigenFace (array): list of eigen faces
    """
    listOfEigenFace = []
    for i in range(int(k)):
        eigenFace = np.matmul(eigen_vectors[i], difference)
        listOfEigenFace.append(eigenFace)
    
    return listOfEigenFace