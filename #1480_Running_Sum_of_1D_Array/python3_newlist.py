class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        running_sum = 0
        for i, n in enumerate(nums):
            running_sum +=n
            output.append(running_sum)
        return output
