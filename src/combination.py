# Import library and os
import cv2
from eigenface import *
import numpy as np

# Function to extract images from dataset to array of matrix
def imageToMatrix(image):
    """
    Function to extract images from dataset to array of matrix

    Args:
        image (file): the test image

    Returns:
        result (array): the image in shape of array 1 x 256^2
    """
    # Image is processed, compressed to 256x256, and flatten to 256^2 x 1
    image = cv2.imread(image)
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    
    # Return Matrix faces
    return result

def videoToMatrix(image):
    """
    Function to extract images from dataset to array of matrix

    Args:
        image (file): the test image

    Returns:
        result (array): the image in shape of array 1 x 256^2
    """
    # Image is processed, compressed to 256x256, and flatten to 256^2 x 1
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    
    # Return Matrix faces
    return result

def processTestImage(test_image):
    """
    Function to process test image

    Args:
        test_image (file): the test image

    Returns:
        image (array): the image in shape of array 1 x 256^2
    """
    # Matrix of test image
    image = imageToMatrix(test_image)

    return image

def differenceTestImage(image, meanFace):
    """
    Function to calculate difference of test image with mean face

    Args:
        image (array): the image in shape of array 1 x 256^2
        meanFace (array): mean face from dataset

    Returns:
        differenceTestImage (matrix): matrix of difference between test image and mean face
    """

    # Difference of test image with mean face
    differenceTestImage = np.subtract(image, meanFace)

    return differenceTestImage

def solveCombinationLinear(difference, array_of_eigenfaces):
    """
    Calculate the linear combination of each training face

    Args:
        difference (matrix): the difference of matrix face and mean face
        array_of_eigenfaces (array): list of eigenfaces

    Returns:
        listOfCombination : list of linear combinations
    """
    # Solve Combination Linear of each training image
    listOfCombination = []
    for item in difference:
        combination = []
        for eigenface in array_of_eigenfaces:
            dot = np.matmul(eigenface, item)
            combination.append(dot)
        listOfCombination.append(combination)
    
    return listOfCombination

def solveCombinationLinearTestImage(array_of_eigenfaces, differenceTestImage):
    """
    Calculate the linear combination of test image

    Args:
        array_of_eigenfaces (array): list of eigenfaces
        differenceTestImage (matrix): the difference of test image and mean face

    Returns:
        combination_test (array): the linear combination of test image
    """
    combination_test = []
    for eigenface in array_of_eigenfaces:
        dot = np.matmul(eigenface, differenceTestImage)
        combination_test.append(dot)

    return combination_test