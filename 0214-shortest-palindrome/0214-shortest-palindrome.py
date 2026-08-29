class Solution(object):
    def shortestPalindrome(self, s):
        t = s[::-1]
        n = len(s)

        for i in range(n + 1):
            if s.startswith(t[i:]):
                return t[:i] + s
        