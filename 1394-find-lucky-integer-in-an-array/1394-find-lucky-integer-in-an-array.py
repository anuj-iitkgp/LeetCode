from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        count = collections.Counter(arr)
        maxi = float('-inf')
        for val, freq in count.items():
            if val == freq:
                maxi = max(maxi, val)
        
        if maxi != float('-inf'):
            return maxi
        return -1
        
        

        