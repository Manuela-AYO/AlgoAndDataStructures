import numpy as np
import time

def selection_sort(tab: np.array) -> np.array: 
    """
    Sort an array using selection sort algorithm(O(n^2))
    :param tab : input array
    :return : the sorted array
    """
    for i in range(0, len(tab)-1):
        key = tab[i]
        index = i
        for j in range(i+1, len(tab)):
            if tab[j] < key:
                key = tab[j]
                index = j
        if index != i:
            temp = tab[i]
            tab[i] = tab[index]
            tab[index] = temp
    return tab

tab = np.array([5, 2, 4, 6, 1, 3])
start = time.time()
tab_sorted = selection_sort(tab)
end = time.time()
print(tab_sorted)  
print(f"Done in {end-start} ms")     