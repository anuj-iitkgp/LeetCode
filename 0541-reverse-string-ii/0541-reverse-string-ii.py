class Solution(object):
    def reverseStr(self, s, k):
        n = len(s)
        ans = ""
        for i in range(0, n, 2 * k ):
                ans += s[i: i + k][::-1] + s[i + k:2*k + i]
        return ans
            



        