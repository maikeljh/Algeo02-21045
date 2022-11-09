from eigenvalue import compute_eigenvalue, get_k_eigenvalue_with_accum_q
import numpy as np

def get_k_eigenvector(arr_eigenvalue, arr_eigenvector):
    arr_eigenvector = np.transpose(arr_eigenvector)
    k, arr_index = get_k_eigenvalue_with_accum_q(arr_eigenvalue)
    n = len(arr_eigenvector[0])
    print(k)
    print(arr_index)
    print(arr_index[1])
    arr_k_eigenvector = np.empty((0, n))
    for i in range(k):
        idx = int(arr_index[i])
        temp = np.array(arr_eigenvector[idx])
        print(temp)
        arr_k_eigenvector = np.append(arr_k_eigenvector, [temp], axis=0)
    
    print(arr_k_eigenvector)
    return arr_k_eigenvector

    




