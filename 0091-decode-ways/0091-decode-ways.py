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
        if not s or s[0] == '0':
            return 0
        
        # prev2 represents dp[i-2] (two steps back)
        # prev1 represents dp[i-1] (one step back)
        prev2 = 1
        prev1 = 1 
        
        for i in range(1, len(s)):
            current = 0
            

            if s[i] != '0':
                current += prev1
                
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            prev2 = prev1
            prev1 = current
            
        return prev1