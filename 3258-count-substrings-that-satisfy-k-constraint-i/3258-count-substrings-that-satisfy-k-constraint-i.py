class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        def ones(t):
            return sum(1 for c in t if c == "1")
        def zeros(t):
            return sum(1 for c in t if c == "0")
        n, t = len(s), 0
        for i in range(n):
            for j in range(i, n):
                if ones(s[i:j+1]) <= k or zeros(s[i:j+1]) <= k :
                    t += 1
        return t


        