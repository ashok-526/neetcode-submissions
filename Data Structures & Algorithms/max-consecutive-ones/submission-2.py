class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        index = 0
        count = []
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] == 1:
                index+=1
            elif nums[i] == 0:
                count.append(index)
                index = 0
        return max(count)