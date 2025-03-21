import numpy as np

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Another solution using the dictionary would have been 
        to store the list of indices of the items of the array
        """
        array_indices_num = np.arange(len(nums))
        self.merge_sort(nums, array_indices_num, 0, len(nums)-1)
        i = 0
        j = len(nums) - 1
        pair_sum = []
        while i != j:
            value_left = nums[array_indices_num[i]]
            value_right = nums[array_indices_num[j]]
            if value_left + value_right == target:
                pair_sum.append(array_indices_num[i])
                pair_sum.append(array_indices_num[j])
                break
            elif value_left + value_right < target:
                i = i + 1
            else:
                j = j - 1
        return pair_sum


    def merge(self, A, array_indices, p, q, r):
        """
        Sort the array of indices based on the values of A
        :type A : List[int]
        :type array_indices : List[int]
        :type p : int
        :type q : int
        :type r : int
        :rtype : None
        """
        length_left = q - p + 1
        length_right = r - q

        array_left = np.zeros(shape=length_left, dtype=int)
        array_right = np.zeros(shape=length_right, dtype=int)

        # create the left and right arrays of indices
        for i in range(length_left):
            array_left[i] = array_indices[p + i]
        for i in range(length_right):
            array_right[i] = array_indices[q+1+i]

        i = 0
        j = 0
        k = p
        # sort those indices based on values of A
        while i < length_left and j < length_right:
            value_left = A[array_left[i]]
            value_right = A[array_right[j]]
            if value_left <= value_right:
                array_indices[k] = array_left[i]
                i = i + 1
            else:
                array_indices[k] = array_right[j]
                j = j + 1
            k = k + 1
        
        while i < length_left:
            array_indices[k] = array_left[i]
            k = k+1
            i = i + 1
        while j < length_right:
            array_indices[k] = array_right[j]
            k = k+1
            j = j + 1
            

    def merge_sort(self, nums, array_indices, p, r):
        """
        Sort the array array_indices of integers using the divide and conquer approach
        based on the values of nums
        :type nums: List[int]
        :rtype: None
        """
        if p == r:
            return
        q = (p + r) // 2
        self.merge_sort(nums, array_indices, p, q)
        self.merge_sort(nums, array_indices, q+1, r)
        self.merge(nums, array_indices, p, q, r)