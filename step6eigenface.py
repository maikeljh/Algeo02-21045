# After we get our eigenvectors, we find the eigenface
from eigenface import *
from eigenvalue import get_k_eigenvalue_with_accum_q
from eigenvector import get_k_eigenvector

def EigenFaces(eigen_vectors, k):
    
    listOfEigenFace = []
    for i in range(int(k)):
        eigenFace = np.matmul(eigen_vectors[i], difference)
        listOfEigenFace.append(eigenFace)
    
    return listOfEigenFace