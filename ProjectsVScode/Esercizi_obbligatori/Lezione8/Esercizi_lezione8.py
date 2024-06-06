# """
# The Number of Beautiful Subsets: write a function with an nums nums 
# of positive integers and a positive integer k given as inputs. A subset of nums
# is beautiful if it does not contain two integers with an absolute difference equal to k. 
# Return the number of non-empty beautiful subsets of the nums nums. A subset of nums is an 
# nums that can be obtained by deleting some (possibly none) elements from nums. Two subsets 
# are different if and only if the chosen indices to delete are different.

# Example 1:
# Input: nums = [2,4,6], k = 2
# Output: 4

# Example 2:
# Input: nums = [1], k = 1
# Output: 1ss
# """

def numeri_bellissimi (nums:list[int],k:int):
    
    lista = []
    
    for i in range(len(nums)):
        for j in range(i + 1 , len(nums)):
            risultato = nums[i] - nums[j]
            if risultato != 0:
                lista.append(abs(risultato))
            
    if len(nums) == 1:
        return nums[0]
    
    for i in lista:
        if i != k:
            return abs(i)
    
nums = [1]
k = 1
print(numeri_bellissimi (nums,k))




# """Combinations: given two integers n and k,
# return all possible combinations of k numbers chosen from the range
# [1, n]. You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# # """
# # def combinations (n:int,k:int)->list[list]:
# #     lista:list[list] = []
# #     lista2:list = range(1,k)
# #     for i in :
# #         lista.append()
        
# """Generate Parentheses: Given n pairs of parentheses, 
# write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]"""