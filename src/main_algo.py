import os
import numpy as np
from eigenvalue import compute_eigenvalue_with_accum_q
from eigenvector import get_k_eigenvector
from step6eigenface import *
import combination as cb
from euclideandst import shortestDst
from extract import imageToMatrix as ITM
import eigenface as EF

# Main Algorithm

def Load_Dataset(dataset):
    """
    The Main Algorithm to load dataset into training images

    Args:
        dataset (string): pathfolder

    Returns:
        meanFace (array)                : the mean face
        array_of_eigenfaces (array)     : array of eigen faces
        listOfCombination (array)       : array of combination
        listOfFixMatrixFace (array)     : array of matrix faces in RGB Mode
    """
    # Step 1
    # Getting list of matrix faces
    listOfMatrixFace, listOfFixMatrixFace = ITM.FolderImageToListOfMatrix(dataset)

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

    # Step 7
    # Compute list of linear combinations of training faces
    listOfCombination = cb.solveCombinationLinear(difference, array_of_eigenfaces)

    return meanFace, array_of_eigenfaces, listOfCombination, listOfFixMatrixFace

def solveImage(test_image, meanFace, array_of_eigenfaces, listOfCombination, listOfFixMatrixFace, dataset, type):
    """
    Function to find the closest image

    Args:
        test_image (string)             : pathfile
        meanFace (array)                : the mean face
        array_of_eigenfaces (array)     : array of eigen faces
        listOfCombination (array)       : array of combination
        listOfFixMatrixFace (array)     : array of matrix faces in RGB Mode
        dataset (string)                : pathfolder
        type (integer)                  : type of test_image 

    Returns:
        result (matrix)     : the picture of the closest face image
        filename (string)   : the name of the closest face image
        dst (float)         : the euclidean distance of the test image and the closest face image
    """
    # Calculating the difference of test image with mean face
    if type == 1:
        testImage = cb.processTestImage(test_image)
    elif type == 2:
        testImage = test_image

    differenceTestImage = cb.differenceTestImage(testImage, meanFace)

    # Compute the combination linear of test image
    combination_test_image = cb.solveCombinationLinearTestImage(array_of_eigenfaces, differenceTestImage)

    # Step 9
    # Calculating the minimum euclidean distance of test image with training images and getting the index of the closest image
    minim, dst = shortestDst(combination_test_image, listOfCombination)
    
    # Step 10
    filename = os.listdir(dataset)[minim]
    result = listOfFixMatrixFace[minim]
    return result, filename, dst