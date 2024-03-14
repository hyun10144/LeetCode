class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums_str = list(map(str, nums))
        count_even = 0
        for i in range(len(nums_str)):
            if len(nums_str[i]) % 2 == 0:
                count_even += 1
                
        return count_even
                