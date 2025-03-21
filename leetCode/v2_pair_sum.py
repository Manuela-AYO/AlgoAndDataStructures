import numpy as np

class Solution(object):
    def twoSum(self, nums, target):
        """
        Find the indexes of a pair sum matching the target
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Another solution using the dictionary would have been 
        to store the list of indices of the items of the array
        """
        # build the list of indexes to later sort this list based on nums[i] 
        # where i is an index of the list
        list_indexes = [i for i in range(len(nums))]
        k = np.log2(len(nums))
        self.sort(nums, list_indexes,  0, len(nums)-1, k)

        i = 0
        j = len(nums) - 1
        pair_sum = []
        while i != j:
            value_left = nums[list_indexes[i]]
            value_right = nums[list_indexes[j]]
            sum_values = value_left + value_right
            if sum_values == target:
                pair_sum = [list_indexes[i], list_indexes[j]]
                break
            elif sum_values < target:
                i = i + 1
            else: 
                j = j - 1
        return pair_sum


    def merge_sort(self, A, indexes_of_A, p, q, r):
        """
        Sort the array indexes_of_A based on A
        :type A : List[int]
        :type p : int
        :type q : int
        :type r : int
        :rtype : None
        """
        length_left = q - p + 1
        length_right = r - q

        # create the left and right arrays of indices
        array_left = [ indexes_of_A[p+i] for i in range(length_left) ]
        array_right = [ indexes_of_A[q+1+i] for i in range(length_right) ]

        i = 0
        j = 0
        k = p
        # sort those indices based on values of A
        while i < length_left and j < length_right:
            if A[array_left[i]] <= A[array_right[j]]:
                indexes_of_A[k] = array_left[i]
                i = i + 1
            else:
                indexes_of_A[k] = array_right[j]
                j = j + 1
            k = k + 1
        
        while i < length_left:
            indexes_of_A[k] = array_left[i]
            k = k+1
            i = i + 1
        while j < length_right:
            indexes_of_A[k] = array_right[j]
            k = k+1
            j = j + 1
            

    def insertion_sort(self, A, indexes_of_A, index_begin, index_end):
        """
        Sort the list indexes_of_A using insertion sort
        based on A's values
        :type A: List[int]
        :type index_begin: int
        :type index_end: int
        :rtype None
        """
        for i in range(index_begin+1, index_end):
            key = A[indexes_of_A[i]]
            index = indexes_of_A[i]
            j = i-1
            while j >= index_begin and A[indexes_of_A[j]] > key:
                indexes_of_A[j+1] = indexes_of_A[j]
                j = j-1
            indexes_of_A[j+1] = index


    def sort(self, nums, indexes_of_nums, p, r, k):
        """
        Sort the array of integers using the divide and conquer approach
        based on the values of nums
        :type nums: List[int]
        :type indexes_of_nums: List[int]
        :type p: int
        :type r: int
        :type k: int
        :rtype: None
        """
        number_items_to_sort = r - p + 1
        if number_items_to_sort <= k:
            self.insertion_sort(nums, indexes_of_nums, p, r+1)
            return
        q = (p + r) // 2
        self.sort(nums, indexes_of_nums, p, q, k)
        self.sort(nums, indexes_of_nums, q+1, r, k)
        self.merge_sort(nums, indexes_of_nums, p, q, r)