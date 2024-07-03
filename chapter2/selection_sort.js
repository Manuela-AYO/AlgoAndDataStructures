function selection_sort(tab) {
    /*
        Function: selection_sort
        Sort an array using selection sort algorithm(O(n^2))
        Parameters:
            tab: input array
        Return:
            the sorted array
    */
   for(let i=0; i<tab.length-1; i++) {
        let key = tab[i]
        let index = i
        for(let j=i+1; j<tab.length; j++) {
            if(tab[j] < key) {
                key = tab[j]
                index = j
            }
        }
        if(index != i) {
            let temp = tab[i]
            tab[i] = tab[index]
            tab[index] = temp
        }
   }
   return tab
}

tab = [5, 2, 4, 6, 1, 3]
tab_sorted = selection_sort(tab)
console.log(tab_sorted)