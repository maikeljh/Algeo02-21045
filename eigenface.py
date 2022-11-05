# Import library
import sys
import matplotlib.pyplot as plt
sys.path.insert(0, './extract')
from extract import imageToMatrix

# Getting list of matrix faces
listOfMatrixFace = imageToMatrix.FolderImageToListOfMatrix("dataset")

# Function to make mean face
def MakeMeanFace(listOfMatrixFace):
    # Declaration for mean face 1 x 256^2
    mean = [0 for i in range(256*256)]

    # The amount of images from dataset
    M = len(listOfMatrixFace)
    
    # Looping for sum of vector images
    for i in range (M):
        for j in range(256*256):
            mean[j] += listOfMatrixFace[i][j]
    
    # Looping for dividing each element with the amount of images
    for i in range(256*256):
        mean[i] /= M

    # Returning vector of mean face
    return mean

# Defining mean face from list of matrix faces
meanFace = MakeMeanFace(listOfMatrixFace)

# Showing image of mean face
plt.imshow(imageToMatrix.reshapeImage(meanFace) , cmap="gray")
plt.show()
