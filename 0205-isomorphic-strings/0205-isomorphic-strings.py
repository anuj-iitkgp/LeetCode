from collections import Counter
class Solution(object):
    def isIsomorphic(self, s, t):
        return [s.find(ch) for ch in s] == [t.find(ch) for ch in t]
        
        