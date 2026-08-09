from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
# Time: O(nlog), Space: O(n) for storing sorted lists, where n is the length of string