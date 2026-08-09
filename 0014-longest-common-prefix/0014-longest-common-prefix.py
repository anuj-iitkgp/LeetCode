class Solution(object):
    def longestCommonPrefix(self, strs):
        # vertical scanning approach

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]