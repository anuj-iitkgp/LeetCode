class Solution(object):
    def findPermutationDifference(self, s, t):
        d = 0
        n = len(s)
        for i in range(n):
            for j in range(n):
                if s[i] == t[j]:
                    d += abs(i - j)
        return d
