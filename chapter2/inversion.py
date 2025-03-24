from typing import List


def count_inversions(A: List[int], begin: int, middle: int, end: int):
    length_left_items = middle - begin + 1
    length_right_items = end - middle

    list_left = [ A[begin + i] for i in range(length_left_items) ]
    list_right = [ A[middle + 1 + i] for i in range(length_right_items) ]

    i = 0
    j = 0
    k = begin
    value = 0
    while i<length_left_items and j<length_right_items:
        if list_left[i] <= list_right[j]:
            A[k] = list_left[i]
            i = i + 1
        else:
            A[k] = list_right[j]
            j = j + 1
            value = value + (length_left_items - i)
        k = k + 1
    
    while i < length_left_items:
        A[k] = list_left[i]
        i = i + 1
        k = k + 1
    while j < length_right_items:
        A[k] = list_right[j]
        j = j + 1
        k = k + 1
    return value

def split(A: List[int], begin: int, end: int):
    if begin == end:
        return 0
    middle = (begin + end) // 2
    value_left = split(A, begin, middle)
    value_right = split(A, middle+1, end)
    inversions = count_inversions(A, begin, middle, end)
    return inversions + value_left + value_right


items = [ 2, 3, 8, 6, 1 ]
nb_inversions = split(items, 0, 4)
print(f"Total number of inversions : {nb_inversions}")