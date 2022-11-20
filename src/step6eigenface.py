# After we get our eigenvectors, we find the eigenface
import numpy as np

def EigenFaces(eigen_vectors, k, difference):
    listOfEigenFace = []
    for i in range(int(k)):
        eigenFace = np.matmul(eigen_vectors[i], difference)
        listOfEigenFace.append(eigenFace)
    
    return listOfEigenFace