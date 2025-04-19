import numpy as np
import time
import math


"""
Prepare the matrices for multiplication or addition
"""
def prepare_matrice(A, B, n, mode):
    matrice_size = n
    if math.ceil(math.log2(n)) != math.floor(math.log2(n)):
        matrice_size = 2**(int(math.ceil(math.log2(n))))
    C = np.zeros(shape=(matrice_size, matrice_size), dtype=int)
    A1 = np.pad(A, ((0, matrice_size-n), (0, matrice_size-n)))
    B1 = np.pad(B, ((0, matrice_size-n), (0, matrice_size-n)))

    match mode:
        case 'add':
            add_matrice(A1, B1, C, matrice_size, 0, 0)
        case 'mult':
            multiply_matrice(A1, B1, C, 0, 0, 0, matrice_size)
        case 'strassen':
            strassen_algorithm(A1, B1, C, matrice_size)
    return C[:n, :n]


"""
Recursively multiply matrice
"""
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


"""
Recursively sums two matrices
"""
def add_matrice(A, B, C, n, i, j):
    if n == 1:
        C[i, j] = A[i, j] + B[i, j]
        return
    split = n // 2
    add_matrice(A, B, C, split, i, j)
    add_matrice(A, B, C, split, i, j+split)
    add_matrice(A, B, C, split, i+split, j)
    add_matrice(A, B, C, split, i+split, j+split)
    

"""
Multiply matrices using Strassen algorithm
"""
def strassen_algorithm(A, B, C, n):
    if n == 1:
        C[0, 0] = A[0, 0] * B[0, 0]
        return

    split =n // 2
    P = [ np.zeros(shape=(split, split)) for _ in range(7) ]

    # recursively compute the Ps
    strassen_algorithm(A[:split, :split], 
                     B[:split, split:] - B[split:, split:], 
                     P[0], 
                     split
                    )
    strassen_algorithm(A[:split, :split] + A[:split, split:], 
                     B[split:, split:], 
                     P[1], 
                     split
                    )
    strassen_algorithm(A[split:, :split] + A[split:, split:], 
                     B[:split, :split], 
                     P[2], 
                     split
                    )
    strassen_algorithm(A[split:, split:], 
                     B[split:, :split] - B[:split, :split], 
                     P[3], 
                     split
                    )
    strassen_algorithm(A[:split, :split] + A[split:, split:], 
                     B[:split, :split] + B[split:, split:], 
                     P[4], 
                     split
                    )
    strassen_algorithm(A[:split, split:] - A[split:, split:], 
                     B[split:, :split] + B[split:, split:], 
                     P[5], 
                     split
                    )
    strassen_algorithm(A[:split, :split] - A[split:, :split], 
                     B[:split, :split] + B[:split, split:], 
                     P[6], 
                     split
                    )

    # compute the Cs
    C[:split, :split] = P[4] + P[3] - P[1] + P[5]
    C[:split, split:] = P[0] + P[1]
    C[split:, :split] = P[2] + P[3]
    C[split:, split:] = P[4] + P[0] - P[2] - P[6]


A = np.random.choice(5, size=(100, 100))
B = np.random.choice(5, size=(100, 100))
start = time.time()
C = prepare_matrice(A, B, A.shape[0], 'strassen')
end = time.time()
print(f"Matrice A : \n", A)
print(f"Matrice B : \n", B)
print(f"Matrice C : \n {C}\n computed in {end-start}ms",)
