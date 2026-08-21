class Solution(object):

    def lengthOfLongestSubstring(self, s):
        mp = {}
        l = 0
        max_len = 0

        for r, char in enumerate(s):
            if char in mp and mp[char] >= l:
                l = mp[char] + 1
            max_len = max(max_len, r - l + 1)
            mp[char] = r

        return max_len
        
        # res = 0
        # n = len(s)

        # for i in range(n):
        #     charSet = set()
        #     for j in range(i, n):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     res = max(res, len(charSet))
        # return res