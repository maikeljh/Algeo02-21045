# Import library and os
import cv2
import matplotlib.pyplot as plt
from eigenface import *
import numpy as np
from eigenvector_driver import array_of_eigenfaces, k
from euclideandst import shortestDst

# Function to extract images from dataset to array of matrix
def imageToMatrix():
    # Image is processed, compressed to 256x256, and flatten to 256^2 x 1
    image = cv2.imread("./testface.jpg")
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    
    # Return Matrix faces
    return result

# Reshape Image from 1 x 256^2 to 256x256 to display
def reshapeImage(face):
    x = 0
    shape = []
    for i in range(256):
        row = []
        for j in range(256):
            row.append(face[x])
            x += 1
        shape.append(row)

    return shape

# Dot product function
def dot_product(vector_1, vector_2):
    sum = 0
    for i in range(len(vector_1)):
        sum += (vector_1[i] * vector_2[i])
    return sum

# Matrix of test image
image = imageToMatrix()

# Difference of test image with mean face
differenceTestImage = np.subtract(image, meanFace)

# Solve Combination Linear of each training image
listOfCombination = []
for item in difference:
    combination = []
    for eigenface in array_of_eigenfaces:
        combination.append(dot_product(item, eigenface))
    listOfCombination.append(combination)

combination_test = []
for eigenface in array_of_eigenfaces:
        combination_test.append(dot_product(differenceTestImage, eigenface))

minim = shortestDst(combination_test, listOfCombination)

plt.imshow(reshapeImage(listOfMatrixFace[minim]), cmap="gray")
plt.show()