import numpy as np
from eigenvalue import get_real_eigenvalue, compute_eigenvalue_with_accum_q, get_k_eigenvalue_with_accum_q
from hessenberg import hessenberg_form
from qr import *
from eigenvector import get_k_eigenvector
import time
from step6eigenface import *
import sys
import matplotlib.pyplot as plt
import numpy as np
from eigenface import covariance

sys.path.insert(0, './extract')
from extract import imageToMatrix as ITM

np.set_printoptions(precision=3)
matrix = covariance

# print(matrix)

# matrix = hessenberg_form(matrix)

# print(hessenberg_matrix)

time1 = time.time()
result, q = compute_eigenvalue_with_accum_q(matrix)
print(result)
print(q)

k, arr = get_k_eigenvector(result, q)

print("Diperlukan waktu selama: ")


# np.set_printoptions(precision=3)
# q = np.transpose(q)
# hasil = np.matmul(matrix, q[0]) - q[0] * result[0]
print(f"Didapat {k} eigenvector adalah")
print(arr)

array_of_eigenfaces = EigenFaces(arr,int(k))
combination_eigenfaces = np.transpose(array_of_eigenfaces)

time2 = time.time()
print(time2 - time1)

    


    

