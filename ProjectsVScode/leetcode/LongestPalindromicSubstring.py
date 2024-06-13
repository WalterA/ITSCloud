class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s==s[::-1]: 
            return s
        left = self.longestPalindrome(s[1:])
        right = self.longestPalindrome(s[:-1])

        if 1<=len(left)>len(right)>=1000:
            left = left
            return left
        else:
            right = right
            return right
    
s = "babad"
solution = Solution()
result = solution.longestPalindrome(s)
print(result)