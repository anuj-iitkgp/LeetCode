
# class Solution(object):
#     def countSubstrings(self, s):
#         def isP(t):
#             return t == t[::-1]
        
#         n = len(s)
#         t = 0
#         for i in range(n):
#             for j in range(i, n):
#                 if isP(s[i:j+1]):
#                     t += 1
#         return t


class Solution(object):
    def countSubstrings(self, s):
        count = 0
        n = len(s)
        for i in range(n):
        # Odd-length palindromes 
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        # Even-length palindromes 
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count