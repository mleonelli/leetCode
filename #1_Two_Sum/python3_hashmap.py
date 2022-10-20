class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # The solution uses the hashamp in order to achive a O(n) execution at the expense of O(n) memory space
        # You loop once only in the number list, adding every number into the hashmap until solution is found
        # Hashmap has an access time of O(1) and it is designed to save the number as indexes and the index
        # on the original list as value
        
        hashmap = {}
        for i in range(len(nums)): 
            reminder = target - nums[i]
            if reminder in hashmap: 
                return [hashmap[reminder], i]
            hashmap[nums[i]] = i
