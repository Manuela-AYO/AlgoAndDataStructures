import numpy as np
import time


def recursive_insertion_sort(A, index):
    if index == 0:
        return
    key = A[index]
    recursive_insertion_sort(A, index-1)
    j = index - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j-1
    A[j+1] = key


A = np.random.choice(np.arange(1, 10), size=6)
print(f"Input table : {A}")
start = time.time()
recursive_insertion_sort(A, 5)
end = time.time()
print(f"Sorted table : {A} in {end-start} ms")