# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         dic = {str(i): chr(i + 64) for i in range(1, 27)}
#         t = 0
#         if s in dic:
#             t += 1
#         for i in range(n):
#             for j in range(i + 1, n):
#                 print(s[:i+1], s[j:])
#                 if s[:i+1] in dic and s[j:] in dic:
#                     t += 1
#         return t

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dic = {str(i): chr(i + 64) for i in range(1, 27)}
        
        # Dictionary to store the results of indices we've already checked
        memo = {}

        if not s or s[0] == '0':
            return 0

        def count(i):
            # 1. If we already calculated the ways for this index, just return it
            if i in memo:
                return memo[i]

            # 2. Base case: we successfully reached the end of the string
            if i == n:
                return 1

            ways = 0

            # 3. Your exact logic
            if s[i] in dic:
                ways += count(i + 1)

            if i + 1 < n and s[i:i+2] in dic:
                ways += count(i + 2)

            # 4. Save the result before returning so we never calculate this index again
            memo[i] = ways
            return ways

        return count(0)