class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        # Two loops solution that has a O(n^2) complexity but has a memory usage of O(1)
    
        arraySize = len(nums)
        for i in range(0, arraySize):
            for j in range(0, arraySize):
                if i == j:
                    break
                if nums[i] + nums[j] == target:
                    return [i, j]
