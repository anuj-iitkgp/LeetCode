class Solution(object):
    def isPalindrome(self, x):
        
        if x < 0:
            return False
        
        elif str(x) != str(x)[::-1]:
            return False
        return True