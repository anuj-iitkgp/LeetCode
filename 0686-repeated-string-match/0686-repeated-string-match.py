from collections import Counter
class Solution(object):
    def repeatedStringMatch(self, a, b):
        
        repeat = len(b) // len(a)
        cnt = 1

        while cnt <= repeat + 2:
            if b in a * cnt:
                return cnt
            cnt += 1
        return -1