class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        for i in range(m):
            result.append(nums1[i])
        for i in range(n):
            result.append(nums2[i])
        result.sort()
        for i in range(m+n):
            nums1[i] = result[i]