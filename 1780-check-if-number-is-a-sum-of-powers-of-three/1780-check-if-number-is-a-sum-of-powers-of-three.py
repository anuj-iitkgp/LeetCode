# class Solution(object):
#     def checkPowersOfThree(self, n):
#         a = n
#         def isPower(m):
#             if m < 1:
#                 return 
#             k = 0
#             while 3**(k + 1) <= m:
#                 k += 1
#             return k
#         t = 0
#         seen = set()
#         while n >= 1:
#             p = isPower(n)
#             if p not in seen:
#                 seen.add(p)
#                 t += (3**p)
#             n -= (3**p)
#         print(t)
#         return t == a


class Solution(object):
    def checkPowersOfThree(self, n):
        while n:
            if n % 3 > 1:
                return False
            n //= 3
        return True