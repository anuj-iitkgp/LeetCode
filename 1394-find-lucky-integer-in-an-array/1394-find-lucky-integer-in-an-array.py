from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        count = Counter(arr)
        print(count)
        maxi = float('-inf')
        for key, value in count.items():
            if key == value:
                maxi = max(maxi, key)
        if maxi == float('-inf'):
            return -1
        return maxi
        
        

        