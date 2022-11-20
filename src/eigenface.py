# Import library
import numpy as np

def MakeMeanFace(listOfMatrixFace):
    """
    Function to make mean face

    Args:
        listOfMatrixFace (array): List of matrix faces

    Returns:
        mean (array): mean face
    """
    # Declaration for mean face 1 x 256^2
    mean = [0 for i in range(256*256)]

    # The amount of images from dataset
    M = len(listOfMatrixFace)
    
    # Looping for sum of vector images
    for i in range (M):
        mean = np.add(mean, listOfMatrixFace[i])
    
    # Looping for dividing each element with the amount of images
    for i in range(256*256):
        mean[i] /= M
    # Returning vector of mean face
    return mean

# Finding the difference for each face matrix
def calculateDifference(listOfMatrixFace, meanFace):
    """
    Finding the difference for each face matrix

    Args:
        listOfMatrixFace (array): list of matrix faces
        meanFace (array): mean face

    Returns:
        difference (matrix): the difference of matrix face and mean face
    """
    difference = []

    # The amount of images from dataset
    M = len(listOfMatrixFace)

    for i in range(M):
        eachDiff = np.subtract(listOfMatrixFace[i], meanFace)
        difference.append(eachDiff)

    return difference

def calculateCovariance(difference):
    """
    Function to calculate covariance

    Args:
        difference (matrix): the difference of matrix face and mean face

    Returns:
        covariance (matrix): the covariance matrix
    """
    # Finding the covariance matrix by multiplying A Transpose with A
    covariance = np.matmul(difference,np.transpose(difference)) # In this case, difference is in form of A Transpose
    return covariance