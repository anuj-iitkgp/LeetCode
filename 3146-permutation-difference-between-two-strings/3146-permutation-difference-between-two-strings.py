class Solution(object):
    def findPermutationDifference(self, s, t):

        # d = 0
        # n = len(s)
        # for i in range(n):
        #     for j in range(n):
        #         if s[i] == t[j]:
        #             d += abs(i - j)
        # return d

        seen = {val: i for i, val in enumerate(s)}
        n = len(s)
        d = 0
        for i in range(n):
            val = seen[t[i]]
            d += abs(i - val)
        return d
