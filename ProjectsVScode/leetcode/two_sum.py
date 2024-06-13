
def twoSum(nums: list[int], target: int) -> list[int] | None:
        
        for i in range(len(nums)):
                for j in range(i + 1, len(nums)):      
                        somma: int = nums[i] + nums[j]
                        
                        if somma == target:
                                
                                return [i, j]
                        
        return None
num = [2,7,11,15]
targe = 9
print(twoSum(num,targe))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
                for j in range(i + 1, len(nums)):      
                        somma: int = nums[i] + nums[j]
                        
                        if somma == target:
                                
                                return [i, j]