import numpy as np
from merge_sort import merge_sort

def checkPairSum(A: np.array, x: int):
    merge_sort(A, 0, len(A)-1)
    left = 0
    right = len(A) - 1
    value = False
    while left != right and not value:
        pair_sum = A[left] + A[right]
        if pair_sum == x:
            value = True
        elif pair_sum < x:
            left = left + 1
        else:
            right = right - 1
    return value


A = np.array([1, 4, 45, 6, 10, -8])
value = checkPairSum(A, 16)

if value:
    print("There exists a pair sum")
else:
    print("There is no pair")