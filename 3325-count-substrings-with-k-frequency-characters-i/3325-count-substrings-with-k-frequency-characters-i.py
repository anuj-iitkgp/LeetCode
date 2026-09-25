from collections import Counter
class Solution(object):
    def numberOfSubstrings(self, s, k):
        n = len(s)
        t = 0
        for i in range(n):
            count = Counter()
            for j in range(i, n):
                count[s[j]] += 1
                if count[s[j]] >= k:
                    t += (n - j)
                    break
        return t
        