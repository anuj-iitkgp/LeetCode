class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        for i in range(1, len(s)):
            if abs(int(s[i]) - int(s[i - 1])) > 2:
                return False
                break
        return True

        
        