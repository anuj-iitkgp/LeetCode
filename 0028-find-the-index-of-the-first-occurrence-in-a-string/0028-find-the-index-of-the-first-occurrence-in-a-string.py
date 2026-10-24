class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans, n = -1, len(haystack)
        m = len(needle)
        for i in range(n):
            if haystack[i:m + i] == needle:
                ans = i
                break
        return ans
        