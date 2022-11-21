# Import library and os
import cv2
import os

def FolderImageToListOfMatrix(folder):
    """
    Function to extract images from dataset to array of matrix

    Args:
        folder (string): pathname to folder of dataset

    Returns:
        listOfMatrixFace (array): list of matrix face that has been resized and grayed
        listOfFixMatrixFace (array): list of matrix face in RGB
    """
    # Initiate List of Matrix Faces
    listOfMatrixFace = []
    listOfFixMatrixFace = []
    
    for filename in os.listdir(folder):
        # Each image is processed, compressed to 256x256, and flatten to 1 x 256^2
        image = cv2.imread(os.path.join(folder,filename))
        image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        listOfFixMatrixFace.append(rgb_image)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        result = gray_image.flatten()

        # Push matrix to list of matrix faces
        listOfMatrixFace.append(result)
    
    # Return List Of Matrix faces
    return listOfMatrixFace, listOfFixMatrixFace

def reshapeImage(face):
    """
    Reshape image matrix from 1 x 256^2 to 256x256

    Args:
        face (array): image in shape of flatten

    Returns:
        shape (matrix): image in shape of 256x256
    """
    x = 0
    shape = []
    for i in range(256):
        row = []
        for j in range(256):
            row.append(face[x])
            x += 1
        shape.append(row)

    return shape
