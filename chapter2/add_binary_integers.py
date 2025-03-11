import numpy as np
import time

def add_binary_integers(A: np.array, B: np.array) -> np.array:
    C = np.zeros(len(A) + 1, dtype=int)
    for i in range(len(A)-1, 0, -1):
        value = A[i] + B[i]
        C[i+1] += value % 2
        C[i] = value // 2
    return C


length = 5
A = np.random.choice([0, 1], size=length)
B = np.random.choice([0, 1], size=length)

start = time.time()
C = add_binary_integers(A, B)
end = time.time()
print(f"Array A : {A}")
print(f"Array B : {B}")
print(f"Sum of A and B : {C}")
print(f"Operation executed in {end-start} ms")