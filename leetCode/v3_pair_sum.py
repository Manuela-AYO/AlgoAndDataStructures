class Solution(object):
    def twoSum(self, nums, target):
        """
        Find indices of two numbers that add up to target.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Sort indices
        sorted_indices = sorted(range(len(nums)), key=lambda i: nums[i])

        # Two-pointer approach
        i, j = 0, len(nums) - 1
        while i < j:
            sum_values = nums[sorted_indices[i]] + nums[sorted_indices[j]]
            if sum_values == target:
                return [sorted_indices[i], sorted_indices[j]]
            elif sum_values < target:
                i += 1
            else:
                j -= 1
        return []