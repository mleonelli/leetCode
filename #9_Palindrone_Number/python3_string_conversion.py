class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # The solution uses the string conversion, which allows an easy string reverse
        # by using array slicing with stride
        
        return str(x) == str(x)[::-1]
      
        # https://leetcode.com/submissions/detail/826475802/
        
