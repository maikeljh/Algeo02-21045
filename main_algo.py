import sys
import matplotlib.pyplot as plt
import numpy as np
import time
from eigenvalue import compute_eigenvalue_with_accum_q
from eigenvector import get_k_eigenvector
from step6eigenface import *
import combination as cb
from euclideandst import shortestDst

sys.path.insert(0, './extract')
from extract import imageToMatrix as ITM
import eigenface as EF

# Main Algorithm
def main_algo(dataset, test_image):
    # Set Start Time
    time1 = time.time()

    # Step 1
    # Getting list of matrix faces
    listOfMatrixFace = ITM.FolderImageToListOfMatrix(dataset)

    # Step 2
    # Defining mean face from list of matrix faces
    meanFace = EF.MakeMeanFace(listOfMatrixFace)

    # Step 3
    # Finding the difference for each face matrix
    difference = EF.calculateDifference(listOfMatrixFace, meanFace)

    # Step 4
    # Finding the covariance matrix
    covariance = EF.calculateCovariance(difference)

    # Step 5
    # QR Decomposition to get eigen values and k eigen vectors
    np.set_printoptions(precision=3)

    # Compute Eigen values
    result, q = compute_eigenvalue_with_accum_q(covariance)

    # Compute k Eigen vectors
    k, arr = get_k_eigenvector(result, q)

    # Step 6
    # Calculate Eigenfaces from Eigen vectors
    array_of_eigenfaces = EigenFaces(arr,int(k), difference)

    # Setting up augmented matrix for getting linear combinations of training face
    combination_eigenfaces = np.transpose(array_of_eigenfaces)

    # Step 7
    # Compute list of linear combinations of training faces
    listOfCombination = cb.solveCombinationLinear(difference, array_of_eigenfaces, k)

    # Step 8
    # Process Test Image to get the combination linear of test image
    testImage = cb.processTestImage(test_image)

    # Calculating the difference of test image with mean face
    differenceTestImage = cb.differenceTestImage(testImage, meanFace)

    # Compute the combination linear of test image
    combination_test_image = cb.solveCombinationLinearTestImage(array_of_eigenfaces, differenceTestImage, k)

    # Step 9
    # Calculating the minimum euclidean distance of test image with training images and getting the index of the closest image
    minim = shortestDst(combination_test_image, listOfCombination)

    # Set Finish Time
    time2 = time.time()

    # Show Execution Time
    print("Execution Time", time2 - time1)

    # Step 10
    cb.showClosestImage(ITM.reshapeImage(listOfMatrixFace[minim]))

main_algo("dataset", "./testface.jpg")