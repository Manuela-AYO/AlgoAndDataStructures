function merge_sort(A, p, q) {
    /*
        Function: merge_sort
        Sort an array using merge sort algorithm(O(nlogn)). 
        Goal: subdivide the array into smaller arrays
        Parameters:
            A: input array
            p: beginning index
            q: end index
        Return:
    */
    if(p>=q)
        return A
    let r = Math.floor((p + q)/2)
    merge_sort(A, p, r)
    merge_sort(A, r+1, q)
    merge(A, p, r, q)
}

function merge(A, p, r, q) {
    /*
        Function : merge
        Combine step of the merge sort algorithm. 
        Goal : sort the array
        Parameters:
            A: input array
            p: beginning index
            r: middle index
            q: end index
        Return:
            the sorted array from p to q
    */
    let left = r - p + 1
    let right = q -r
    let A_left = new Array(left)
    let A_right = new Array(right)

    for(let i=0; i<left; i++) {
        A_left[i] = A[p+i]
    }
      
    for(let i=0; i<right; i++) {
        A_right[i] = A[r + 1 + i]
    }

    let i=0
    let j = 0
    let k = p

    while(i<left && j<right) {
        if(A_left[i] <= A_right[j]) {
            A[k] = A_left[i]
            i += 1
        }
        else {
            A[k] = A_right[j]
            j += 1
        }

        k += 1
    }

    while(i<left) {
        A[k] = A_left[i]
        i += 1
        k+= 1
    }

    while(j<right) {
        A[k] = A_right[j]
        j += 1
        k+=1 
    }
    return A
}

tab = new Array(5, 2, 4, 6, 1, 3);
merge_sort(tab, 0, 5)
console.log(tab)