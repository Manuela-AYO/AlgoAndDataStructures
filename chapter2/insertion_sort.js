function insertion_sort(tab) {
    /*
        Function: insertion_sort
        Sort an array using insertion sort algorithm(O(n^2))
        Parameters:
            tab: input array
        Return:
            the sorted array
    */
   for(let i=1; i<tab.length; i++) {
        let key = tab[i];
        let j = i-1;
        while(j>=0 && tab[j] > key) {
            tab[j+1] = tab[j];
            j = j-1;
        }
        tab[j+1] = key
   }
   return tab
}

tab = [5, 2, 4, 6, 1, 3];
tab_sorted = insertion_sort(tab);
console.log(tab_sorted);