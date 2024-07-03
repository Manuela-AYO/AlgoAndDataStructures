#include <iostream>

#include "sort.h"

int main(int argc, char** argv) {
    int len = 6;
    int tab[6] = { 5, 2, 4, 6, 1, 3};
    selection_sort(tab, len);
    for(int i=0; i<len; i++) {
        std::cout << tab[i] << " ";
    }
    std::cout << "\n";
}