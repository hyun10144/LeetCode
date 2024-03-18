class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(len(arr)-2):
            if arr[i] < arr[i+1]:
                if arr[i+1] > arr[i+2]:
                    for j in range(i+1, len(arr)-1):
                        if arr[j] <= arr[j+1]:
                            return False
                    return True
            else:
                return False
                        
        return False