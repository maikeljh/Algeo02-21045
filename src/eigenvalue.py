from qr import qr_iteration_with_accum_q
from hessenberg import hessenberg_form
import numpy as np

THRESHOLD = 0.95
ITERATION = 10

def get_k_eigenvalue_with_accum_q(array):
    """Pick specific amount of eigenvalue and eigenvector

    Args:
        array (array): array of eigenvalue 

    Returns:
        tuple: number of eigenvalue selected, array of selected eigenvalue index
    """
    n = len(array)
    array_sum = np.sum(array)
    indexed_array = []
    for i in range(n):
        indexed_array += [[i+1, array[i]]]

    indexed_array = np.array(indexed_array)
    sorted_array = indexed_array[indexed_array[:,1].argsort(kind='mergesort')[::-1]]
    i = 0
    accumulative_sum = 0
    accumulative_array = []
    while (accumulative_sum/array_sum <= THRESHOLD):
        accumulative_sum += sorted_array[i][1]
        accumulative_array = np.append(accumulative_array, [sorted_array[i][0]])
        i += 1
    return i, accumulative_array

def compute_eigenvalue_with_accum_q(matrix):
    """Get eigenvalue and eigenvector from matrix

    Args:
        matrix (matrix): square matrix

    Returns:
        tuple : array of eigenvalue, and eigenvector
    """
    hessenberg_matrix = hessenberg_form(matrix)
    schur_form, q = qr_iteration_with_accum_q(hessenberg_matrix, ITERATION)

    return schur_form.diagonal(), q