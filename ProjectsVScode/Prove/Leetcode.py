# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []  # No solution found
# def longestCommonPrefix(v: list[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans
# l=["ciao","ok"]
# longestCommonPrefix(l)
""" FUNZIONA------------------------------------------------------------------------------------------------------------------------
def removeDuplicates(nums: list[int]) -> int: #quanti duplicati ci sono
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
n=[2,2,2,2,5,6,7]
print(removeDuplicates(n))-----------------------------------------------------------------------------------------------------
"""