import numpy as np
import time
import math


def prepare_matrice(A, B, n):
    matrice_size = n
    if math.ceil(math.log2(n)) != math.floor(math.log2(n)):
        matrice_size = 2**(int(math.ceil(math.log2(n))))
    C = np.zeros(shape=(matrice_size, matrice_size), dtype=int)
    A1 = np.pad(A, ((0, matrice_size-n), (0, matrice_size-n)))
    B1 = np.pad(B, ((0, matrice_size-n), (0, matrice_size-n)))
    multiply_matrice(A1, B1, C, 0, 0, 0, matrice_size)
    return C[:n, :n]

def multiply_matrice(A, B, C, begin_row_matriceA, begin_column_matriceA, begin_column_matriceB, n):
    if n == 1:
        C[begin_row_matriceA, begin_column_matriceB] += A[begin_row_matriceA, begin_column_matriceA] * B[begin_column_matriceA, begin_column_matriceB]
        return
    split = n // 2
    multiply_matrice(A, B, C, begin_row_matriceA, begin_column_matriceA, begin_column_matriceB, split)
    multiply_matrice(A, B, C, begin_row_matriceA, begin_column_matriceA, begin_column_matriceB + split, split)
    multiply_matrice(A, B, C, begin_row_matriceA, begin_column_matriceA + split, begin_column_matriceB, split)
    multiply_matrice(A, B, C, begin_row_matriceA, begin_column_matriceA + split, begin_column_matriceB + split, split)
    multiply_matrice(A, B, C, begin_row_matriceA + split, begin_column_matriceA, begin_column_matriceB, split)
    multiply_matrice(A, B, C, begin_row_matriceA + split, begin_column_matriceA, begin_column_matriceB + split, split)
    multiply_matrice(A, B, C, begin_row_matriceA + split, begin_column_matriceA + split, begin_column_matriceB, split)
    multiply_matrice(A, B, C, begin_row_matriceA + split, begin_column_matriceA + split, begin_column_matriceB + split, split)


A = np.random.choice(7, size=(5, 5))
B = np.random.choice(7, size=(5, 5))
start = time.time()
C = prepare_matrice(A, B, A.shape[0])
end = time.time()
print(f"Matrice A : \n", A)
print(f"Matrice B : \n", B)
print(f"Matrice C : \n", C)
