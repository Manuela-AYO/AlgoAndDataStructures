class Solution:
    """
    Find indices of two numbers that add up to target.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def twoSum(self, nums, target):
        index_map = {}  # Stores {num: index}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                return [index_map[diff], i]
            index_map[num] = i
        return []