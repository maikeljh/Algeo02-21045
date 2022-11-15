# Import library
import numpy as np

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

# Finding the difference for each face matrix
def calculateDifference(listOfMatrixFace, meanFace):
    difference = []
    for i in range(len(listOfMatrixFace)):
        eachDiff = [0 for k in range(256*256)]
        for j in range(256*256):
            eachDiff[j] = listOfMatrixFace[i][j] - meanFace[j]
        difference.append(eachDiff)
    return difference

def calculateCovariance(difference): 
    # Finding the covariance matrix by multiplying A Transpose with A
    covariance = np.matmul(difference,np.transpose(difference)) # In this case, difference is in form of A Transpose
    return covariance



