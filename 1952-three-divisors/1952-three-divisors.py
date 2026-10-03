class Solution(object):
    def isThree(self, n):
        t = 0
        for i in range(1, n + 1):
            if n % i == 0:
                t += 1
        if t == 3:
            return True
        return False
