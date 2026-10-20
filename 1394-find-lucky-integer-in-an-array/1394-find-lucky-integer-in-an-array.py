from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        count = collections.Counter(arr)
        maxi = -1
        for val, freq in count.items():
            if val == freq:
                maxi = max(maxi, val)
        return maxi

        