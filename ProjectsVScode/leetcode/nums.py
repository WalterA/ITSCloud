    
nums = [3,0,1]
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num=sorted(nums)
        for i in range(len(num)):
            if num[i] != i:
                return i
        return len(num)