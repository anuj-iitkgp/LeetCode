class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        x, y = 0, 0
        length = 0

        for i in range(n):
            l = i
            r = i

            # handle odd length string

            while ((l >=0  and r < n) and (s[l] == s[r])):
                if length < (r - l + 1):
                    x = l
                    y = r
                    length = r - l + 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while ((l >= 0 and r < n) and (s[l] == s[r])):
                if length < (r - l + 1):
                    x = l
                    y = r
                    length = r - l + 1
                l -= 1
                r += 1
            
        ans = ""
        for i in range(x, y + 1):
            ans += s[i]
        return ans
            
