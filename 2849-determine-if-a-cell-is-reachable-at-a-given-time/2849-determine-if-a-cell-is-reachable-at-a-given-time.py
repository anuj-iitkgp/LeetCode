class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        if (sx == fx and sy == fy and t == max(abs(sx - fx), abs(sy - fy)) + 1) or max(abs(sx - fx), abs(sy - fy)) > t:
            return False
        return True
        