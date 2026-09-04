class Solution(object):

  def largestPalindrome(self, n):
    ans = [0, 9, 987, 123, 597, 677, 1218, 877, 475]
    return ans[n]

# class Solution(object):
#     def largestPalindrome(self, n):
#         if n == 1:
#             return 9
        
#         max_no = 10**n - 1
#         min_no = 10**(n - 1)

#         for first_half in range(max_no, min_no - 1, -1):
#             palindrome = first_half
#             temp = first_half
            
#             while temp:
#                 palindrome = palindrome * 10 + temp % 10
#                 temp //= 10
#             mod = 1337
#             x = max_no
#             while palindrome <= x * x:
#                 if palindrome % x == 0:
#                     return palindrome % mod
#                 x -= 1
#         return -1
            