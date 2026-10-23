class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n, t = len(s), 0
        for i in range(n):
            ones, zeros = 0, 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1
                else:
                    zeros += 1
                if ones <= k or zeros <= k:
                    t += 1
                else:
                    break   
        return t


# class Solution:
#     def countKConstraintSubstrings(self, s: str, k: int) -> int:
#         def ones(t):
#             return sum(1 for c in t if c == "1")
#         def zeros(t):
#             return sum(1 for c in t if c == "0")
#         n, t = len(s), 0
#         for i in range(n):
#             for j in range(i, n):
#                 if ones(s[i:j+1]) <= k or zeros(s[i:j+1]) <= k :
#                     t += 1
#         return t


        