class Solution(object):
    def minBitFlips(self, start, goal):
        
        ans = start ^ goal
        cnt = 0
        for i in range(32):
            if ans & (1 << i):
                cnt += 1
        return cnt