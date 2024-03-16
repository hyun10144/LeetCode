class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        result = []
        for num in arr:
            if num == 0:
                result.append(0)
            result.append(num)
        for i in range(len(arr)):
            arr[i] = result[i]
    