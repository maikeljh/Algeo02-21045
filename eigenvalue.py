from qr import qr_iteration
from hessenberg import hessenberg_form
import numpy as np

def eigenvalue_array(matrix):
    n = len(matrix)

    hessenberg_matrix = hessenberg_form(matrix)
    eigen_diagonal = qr_iteration(hessenberg_matrix, 40)

    eigenvalue_result = eigen_diagonal.diagonal()
    return eigenvalue_result

