# Import library and os
import cv2
import matplotlib.pyplot as plt
from eigenface import *
import numpy as np
from euclideandst import shortestDst

# Function to extract images from dataset to array of matrix
def imageToMatrix(image):
    # Image is processed, compressed to 256x256, and flatten to 256^2 x 1
    image = cv2.imread(image)
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    
    # Return Matrix faces
    return result

def videoToMatrix(image):
    # Image is processed, compressed to 256x256, and flatten to 256^2 x 1
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    
    # Return Matrix faces
    return result

def processTestImage(test_image):
    # Matrix of test image
    image = imageToMatrix(test_image)

    return image

def differenceTestImage(image, meanFace):
    # Difference of test image with mean face
    differenceTestImage = np.subtract(image, meanFace)

    return differenceTestImage

def solveCombinationLinear(difference, array_of_eigenfaces, k):
    # Solve Combination Linear of each training image
    listOfCombination = []
    for item in difference:
        combination = []
        for eigenface in array_of_eigenfaces:
            dot = np.matmul(eigenface, item)
            combination.append(dot)
        listOfCombination.append(combination)
    
    return listOfCombination

def solveCombinationLinearTestImage(array_of_eigenfaces, differenceTestImage, k):
    combination_test = []
    for eigenface in array_of_eigenfaces:
        dot = np.matmul(eigenface, differenceTestImage)
        combination_test.append(dot)

    return combination_test

def showClosestImage(image):
    plt.imshow(cv2.cvtColor(np.matrix(image), cv2.COLOR_GRAY2RGB))
    plt.show()