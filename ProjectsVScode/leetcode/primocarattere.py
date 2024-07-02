class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                return i
        return -1 

s = "leetcode"
f = Solution()
kint=f.firstUniqChar(s)
print(kint)