from collections import Counter
class Solution(object):
    def repeatedStringMatch(self, a, b):
        
        # repeat = len(b) // len(a)
        # cnt = 1

        # while cnt <= repeat + 2:
        #     if b in a * cnt:
        #         return cnt
        #     cnt += 1
        # return -1

        min_repeat = (len(b) + len(a) - 1) // len(a)

        if b in a * min_repeat:
            return min_repeat
        if b in a * (min_repeat + 1):
            return (min_repeat + 1)
        return -1