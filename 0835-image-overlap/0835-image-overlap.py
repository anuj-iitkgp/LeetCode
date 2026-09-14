from collections import defaultdict

class Solution(object):
    def largestOverlap(self, img1, img2):
        L1 = [(i << 10) + j for i, row in enumerate(img1) for j, c in enumerate(row) if c == 1]
        L2 = [(i << 10) + j for i, row in enumerate(img2) for j, c in enumerate(row) if c == 1]
        
        diff = defaultdict(int)
        for x in L1:
            for y in L2:
                diff[x - y] += 1
                
        return max(diff.values() or [0])