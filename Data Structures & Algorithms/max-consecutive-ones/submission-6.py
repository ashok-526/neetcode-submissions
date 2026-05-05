class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = best = 0
        for num in nums:
            if num == 1:
                current+=1
            else:
                best = max(current, best)
                current = 0

        return max(current , best)