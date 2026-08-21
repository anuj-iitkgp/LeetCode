class Solution(object):
    def lengthOfLongestSubstring(self, s):

        n = len(s)
        l, r = 0, 0
        max_len = 0
        mp = [-1] * 256

        while r < n:
            char_code = ord(s[r])
            if mp[char_code] >= l:
                l = mp[char_code] + 1
            length = r - l + 1
            max_len = max(max_len, length)
            mp[char_code] = r
            r += 1
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