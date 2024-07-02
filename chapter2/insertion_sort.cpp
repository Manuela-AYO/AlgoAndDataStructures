#include <iostream>

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

int main(int argc, char** argv) {
    int len = 6;
    int tab[6] = { 5, 2, 4, 6, 1, 3};
    insertion_sort(tab, len);
    for(int i=0; i<len; i++) {
        std::cout << tab[i] << " ";
    }
    std::cout << "\n";
}