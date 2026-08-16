class Solution(object):
    def maxDepth(self, s):
        
        count = 0
        maxi = 0
        for t in s:
            if t == "(":
                count += 1
                maxi = max(maxi, count)

            if t == ")":
                count -= 1
                maxi = max(maxi, count)
        return maxi
