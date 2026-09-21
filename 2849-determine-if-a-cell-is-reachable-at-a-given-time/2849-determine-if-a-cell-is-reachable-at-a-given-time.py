class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        a = max(abs(sx - fx), abs(sy - fy))
        if (sx == fx and sy == fy and t == a + 1) or a > t:
            return False
        return True
        