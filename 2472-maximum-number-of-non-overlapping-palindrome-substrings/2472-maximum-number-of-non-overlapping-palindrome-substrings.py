
class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)

        def ip(i, j):
            if j >= n:
                return False
            if i >= j:
                return True
            return ip(i + 1, j - 1) if s[i] == s[j] else False

        result = 0
        i = 0
        while i < n - k + 1:
            if ip(i, i + k - 1):
                result += 1
                i += k - 1
            elif ip(i, i + k):
                result += 1
                i += k
            i += 1

        return result






# class Solution(object):
#     def maxPalindromes(self, s, k):
#         n = len(s)
#         if k == 1: return n

#         res = i = 0

#         while i <= n - k:
#             for d in (k, k + 1):
#                 if i + d <= n and s[i : i + d] == s[i : i + d][::-1]:
#                     res += 1
#                     i += d
#                     break
#             else:
#                 i += 1

#         return res

        