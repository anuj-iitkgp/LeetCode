class Solution(object):
    def longestCommonPrefix(self, strs):
        # Sorting Approach

        if len(strs) == 1:
            return strs[0]

        strs_sorted = sorted(strs)

        for i in range(min(len(strs_sorted[0]), len(strs_sorted[-1]))):
            if strs_sorted[0][i] != strs_sorted[-1][i]:
                return strs_sorted[0][:i]
        return strs_sorted[0]

# Time complexity: O(n * mlogm), Space: constant
