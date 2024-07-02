import numpy as np

def insertion_sort(tab: np.array) -> np.array:
    """
    Sort an array using insertion sort algorithm(O(n^2))
    :param tab : input array
    :return : the sorted array
    """
    for i in range(1, len(tab)):
        key = tab[i]
        j = i-1
        while j>=0 and tab[j] > key:
            tab[j+1] = tab[j]
            j = j-1
        tab[j+1] = key
    return tab

tab = np.array([5, 2, 4, 6, 1, 3])
tab_sorted = insertion_sort(tab)
print(tab_sorted)