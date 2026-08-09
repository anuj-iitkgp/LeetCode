class Solution(object):
    def longestCommonPrefix(self, strs):
        n = len(strs)
        
        prefix = strs[0]

        for i in range(1, n):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
        