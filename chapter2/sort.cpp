#include "sort.h"

void insertion_sort(int *tab, int n) {
    /*
     * @brief Sort an array using insertion sort algorithm(O(n^2))
     * @param tab : input array
     * @param n : size of the array
     * @return : the sorted array
     */

    int key, j;

    for(int i=1; i<n; i++) {
        key = tab[i];
        j = i-1;
        while(j>=0 && tab[j]>key) {
            tab[j+1] = tab[j];
            j -= 1;
        }
        tab[j+1] = key;
    }
}


void selection_sort(int *tab, int n) {
    /*
     * @brief Sort an array using insertion sort algorithm(O(n^2))
     * @param tab : input array
     * @param n : size of the array
     * @return : the sorted array
     */

    int key, j, index, temp;

    for(int i=0; i<n-1; i++) {
        key = tab[i];
        index = i;
        for(j=i+1; j<n; j++) {
            if(key > tab[j]) {
                key = tab[j];
                index = j;
            }
        }
        if(index != i) {
            temp = tab[i];
            tab[i] = tab[index];
            tab[index] = temp;
        }
    }
}