from qr import qr_iteration, qr_iteration_with_accum_q
from hessenberg import hessenberg_form
import numpy as np

SENSITIVITY = 1
THRESHOLD = 0.95
ITERATION = 40

def compute_eigenvalue(matrix):
    hessenberg_matrix = hessenberg_form(matrix)
    schur_form = qr_iteration(hessenberg_matrix, ITERATION)
    
    return schur_form.diagonal()

def get_k_eigenvalue(array):
    n = len(array)
    array_sum = np.sum(array)
    sorted_array = np.sort(array)[::-1]
    i = 0
    accumulative_sum = 0
    accumulative_array = []
    while (accumulative_sum/array_sum <= THRESHOLD):
        accumulative_sum += sorted_array[i]
        accumulative_array = np.append(accumulative_array, sorted_array[i])
        i += 1
    k = i
    return i, accumulative_array


def get_k_eigenvalue_with_accum_q(array):
    # array = np.abs(array)
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
    k = i
    return i, accumulative_array

def matrix_schur_form(matrix):
    # https://www.sciencedirect.com/topics/engineering/real-schur-form
    hessenberg_matrix = hessenberg_form(matrix)
    schur_form = qr_iteration(hessenberg_matrix, ITERATION)

    
    return schur_form

def diagonal_mean_absolute(matrix):
    array_diagonal = matrix.diagonal()
    abs_array = np.absolute(array_diagonal)
    mean = np.mean(abs_array)
    return mean

def real_eigenvalue(matrix):
    # Asumsi n > 1
    n = len(matrix)
    np.set_printoptions(precision=1)
    print(matrix)
    threshold = diagonal_mean_absolute(matrix) / SENSITIVITY
    array = np.empty(0)
    print("Threshold")
    print(threshold)

    if (matrix[1, 0] < threshold):
        array = np.append(array, matrix[0, 0])
    for i in range(1, n-1):
        print(matrix[i, i - 1])
        if ((matrix[i, i - 1] < threshold) and (matrix[i + 1, i] < threshold)):
            array = np.append(array, matrix[i, i])
    if (matrix[n-1, n-2] < threshold):
        array = np.append(array, matrix[n-1, n-1])
    
    return array

def get_real_eigenvalue(matrix):
    schur_form = matrix_schur_form(matrix)
    array_eigenvalue = real_eigenvalue(schur_form)

    return array_eigenvalue

def compute_eigenvalue_with_accum_q(matrix):
    hessenberg_matrix = hessenberg_form(matrix)
    schur_form, q = qr_iteration_with_accum_q(hessenberg_matrix, ITERATION)


    
    return schur_form.diagonal(), q

# def get_k_eigenvalue_with_accum_q(matrix):
#     n = len(array)
#     array_sum = np.sum(array)
#     sorted_array = np.sort(array)[::-1]
#     i = 0
#     accumulative_sum = 0
#     accumulative_array = []
#     while (accumulative_sum/array_sum <= THRESHOLD):
#         accumulative_sum += sorted_array[i]
#         accumulative_array = np.append(accumulative_array, sorted_array[i])
#         i += 1
#     k = i
#     return i, accumulative_array



