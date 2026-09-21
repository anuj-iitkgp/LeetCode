class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        a = max(abs(sx - fx), abs(sy - fy))
        if a > t:
            return False
        if sx == fx and sy == fy and t == a + 1:
            return False
        return True
        