class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        count_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count_ones += 1
            else:
                output = max(output, count_ones)
                count_ones = 0
        output = max(output, count_ones)
        return output
                