class Solution(object):
    def countSubstrings(self, s):
        def isP(t):
            return t == t[::-1]
        
        n = len(s)
        t = 0
        for i in range(n):
            for j in range(i, n):
                if isP(s[i:j+1]):
                    t += 1
        return t