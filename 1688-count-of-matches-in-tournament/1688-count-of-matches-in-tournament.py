class Solution(object):
    def numberOfMatches(self, n):
        t = 1
        if n == 1:
            return 0
        while n != 2:
            if n % 2 == 0:
                t += n // 2
                n //= 2
            t += (n - 1) // 2
            n = n // 2 + 1
        return t

        








# class Solution(object):
#     def numberOfMatches(self, n):
#         mat = 0
#         adv = 0
#         t = 1
#         if n == 1:
#             return 0
#         while n != 2:
#             if n % 2 == 0:
#                 mat = n // 2
#                 t += mat
#                 adv = n // 2
#                 n //= 2
#             if n % 2 == 1:
#                 mat = (n - 1) // 2
#                 t += mat
#                 adv = (n - 1) // 2 + 1
#                 n = n // 2 + 1
            
#         return t

        