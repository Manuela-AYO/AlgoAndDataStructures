class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [ int(number) for number in str(n) ]
        if digits[0] >= digits[1]:
            max1 = digits[0]
            max2 = digits[1]
        else:
            max1 = digits[1]
            max2 = digits[0]
        for i in range(2, len(digits)):
            if digits[i] > max1:
                max2 = max1
                max1 = digits[i]
            elif digits[i] > max2:
                max2 = digits[i]
        return max1 * max2
    
class Solution2(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        max1 = 0
        max2 = 0
        while n > 0:
            if n%10 > max1:
                max2 = max1
                max1 = n%10
            elif n%10 > max2:
                max2 = n%10
            n = n // 10
        return max1 * max2  