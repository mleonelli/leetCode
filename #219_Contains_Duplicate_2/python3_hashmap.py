class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #This problem is extremely similar in solution to #1 Two Sum
        #You forward pass once the list in O(n) time, validate if the requirement is met and if not
        #the item is saved in hashmap for access in O(1) time
        
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap and i - hashmap[num] <= k:
                return True
            hashmap[num] = i
        return False
    
        #https://leetcode.com/submissions/detail/827226308/
        #To evaluate the set approach as better in memory consumption
