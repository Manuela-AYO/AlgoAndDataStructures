import numpy as np
import time

def merge_sort(A:np.array, p:int, q:int):
    if p >= q :
        return
    r = (p + q)//2
    merge_sort(A, p, r)
    merge_sort(A, r+1, q)
    merge(A, p, r, q)


def merge(A:np.array, p:int, r:int, q:int):
    left = r - p + 1
    right = q - r
    A_left = np.ones(left)
    A_right = np.ones(right)

    for i in range(0, left):
        A_left[i] = A[p+i]

    for i in range(0, right):
        A_right[i] = A[r + 1 + i]

    i=0
    j=0
    k=p
    while i<left and j<right:
        if A_left[i] <= A_right[j]:
            A[k] = A_left[i]
            i = i+1
        else:
            A[k] = A_right[j]
            j = j+1
        k = k + 1
        
    while i<left: 
        A[k] = A_left[i]
        k = k+1
        i = i+1

    while j<right:
        A[k] = A_right[j]
        k = k+1
        j = j+1
    
    return A

tab = np.array([5, 2, 4, 6, 1, 3])
start = time.time()
merge_sort(tab, 0, 5)
end = time.time()
print(tab)
print(f"Done in {end-start} ms") 