# After we get our eigenvectors, we find the eigenface
from eigenface import *

def EigenFaces(eigen_vectors):
    listOfEigenFace = []
    eigenFace = []
    for i in range(len(listOfMatrixFace)):
        eigenFace = np.matmul(eigen_vectors[i], difference)
        listOfEigenFace.append(eigenFace)
    
    return listOfEigenFace
