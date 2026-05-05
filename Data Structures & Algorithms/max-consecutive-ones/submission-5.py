class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        index = 0
        best=0
        for i in range(len(nums)):
            if nums[i] == 1:
                index+=1
            elif nums[i] == 0:
                index = 0
            best = max(index , best)

            
            
        return best