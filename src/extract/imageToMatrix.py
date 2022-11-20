# Import library and os
import cv2
import os
import matplotlib.pyplot as plt

# Function to extract images from dataset to array of matrix
def FolderImageToListOfMatrix(folder):
    # Initiate List of Matrix Faces
    listOfMatrixFace = []
    listOfFixMatrixFace = []
    for filename in os.listdir(folder):
        # Each image is processed, compressed to 256x256, and flatten to 256^2 x 1
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
