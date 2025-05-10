class Solution(object):
    def isPalindrome(self, s, i, j):
        left = i
        right = j - 1
        result = True
        while left < right:
            if s[left] != s[right]:
                result = False
                break
            else:
                left += 1
                right -= 1
        return result


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ""
        left = 0
        right = len(s)-1
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                if self.isPalindrome(s, j, j+i):
                    return s[j:j+i]
        return palindrome
    
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp  = [ [False] * n for _ in range(n) ]
        ans = [0, 0]
        dp[0][0] = True
        for i in range(n-1):
            dp[i+1][i+1] = True
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]
        for diff in range(2, n):
            for i in range(n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]
        return s[ans[0]: ans[1]+1]
    
class Solution3(object):
    def expand(self, s, i, j):
        left = i
        right = j
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = [0, 0]
        for i in range(len(s)):
            odd_length = self.expand(s, i, i)
            if odd_length > ans[1]-ans[0]+1 :
                ans = [ i - odd_length//2, i + odd_length // 2]

            even_length = self.expand(s, i, i+1)
            if even_length > ans[1] - ans[0]+1:
                dist = even_length // 2 - 1
                ans = [ i - dist, i + dist + 1]
        return s[ans[0]:ans[1]+1]
    
class Solution4(object):
    def longestPalindrome(s):
            """
            :type s: str
            :rtype: str
            """
            s_prime = "#" + "#".join(s) + "#"
            n = len(s_prime)
            palindrome_radii = [0] * n
            center = radius = 0

            for i in range(n):
                mirror = 2*center - i
                if i < radius:
                    palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])
                while(
                    i + 1 + palindrome_radii[i] < n
                    and i - 1 - palindrome_radii[i] >= 0
                    and s_prime[i + 1 + palindrome_radii[i]]
                    == s_prime[i - 1 - palindrome_radii[i]]
                ):
                    palindrome_radii[i] += 1
                if i + palindrome_radii[i] > radius:
                    center = i 
                    radius = i + palindrome_radii[i]
            max_length = max(palindrome_radii)
            center_index = palindrome_radii.index(max_length)
            start_index = (center_index - max_length) // 2
            longest_palindrome = s[start_index : start_index + max_length]
            return longest_palindrome
