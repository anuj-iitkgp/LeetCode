# class Solution:
#     def repeatedStringMatch(self, a: str, b: str) -> int:
#         if len(b) % len(a) != 0:
#             n = len(b) // len(a) + 2
#         else:
#             n =  min(len(b), len(b) // len(a) + 1) 
#         s = a * n
#         k = len(b)
#         t = 0
#         for i in range(len(s)):
#             if b == s[i:k + i]:
#                 return (i + k - 1) // len(a) + 1
#         return -1

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeat = (len(b) + len(a) - 1) // len(a)
        if b in a * min_repeat:
            return min_repeat
        if b in a * (min_repeat + 1):
            return (min_repeat + 1)
        return -1
                
        