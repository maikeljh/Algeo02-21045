# Algeo02-21045 - #TeamOnodera

## Table of Contents
* [Project Description](#Project-Description)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Screenshots](#screenshots)
* [Acknowledgements](#acknowledgements)


## Project Description
A facial recognition application based on eigenface, made in python. This repository is for Tugas Besar IF2123 Aljabar Linear Geometri 2022/2023

The assigment of the project is to make a python, GUI-based application which is able to match a random face to a closest one available in the dataset. The methods applied to achieve said goal is the eigenface algorithm, which calculates the average face then eigenvalues and vectors from corresponding deviation values from the average face to the each image from the dataset and weights it over the average face, then fetches the image with the closest value to the test image in terms of weighting.

Contributors:
- Fakhri Muhammad Mahendra 13521045
- Muhamad Aji Wibisono 13521095
- Michael Jonathan Halim 13521124<br><br>




## Features
- Tkinter based GUI
- GUI available in fullscreen and windowed
- User-selected dataset
- User-selected test image
- Live feed from camera as test image possible
- Time of dataset loading, algorithm execution, and euclidean distance of the weighting are shown in real time<br><br>

## Setup
### Dependencies
- Numpy
- OpenCV
- Matplotlib
- Tkinter
- Pillow

### Installation
- Download and install Python (https://www.python.org/downloads/)
- Download install dependencies from the terminal
    > 
        -pip install numpy
        
        -pip install opencv-python

        -pip install matplotlib

        -pip install tkinter

        -pip install pillow
- If program doesn't run as intended, try installing an older version of python (https://www.python.org/downloads/release/python-394/)<br><br>

## Usage
- Clone or download the repository
    > 
        git clone https://github.com/maikeljh/Algeo02-21045.git
- Run main.py file inside src<br><br>

## Screenshots
![image](https://user-images.githubusercontent.com/89117568/203071370-067c55b2-42c7-416f-b4ab-0c9af56063af.png)
![image](https://user-images.githubusercontent.com/89117568/203071073-b66c724b-d509-46d4-ae41-6807b0b1c6ff.png)<br><br>

## Acknowledgements
- Bandung Institute of Technology, Informatics Engineering
- Munir, Rinaldi. (2022). IF2123 Aljabar Geometri - Semester I Tahun 2022/2023. Institut Teknologi Bandung. Diakses pada 3 Oktober 2022, dari https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2022-2023/algeo22-23.htm
