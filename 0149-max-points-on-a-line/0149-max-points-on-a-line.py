import math
import fractions
from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
        
        
        max_points = 1

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):

                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1
        # Reduce fraction by gcd to avoid float precision issue
                g = fractions.gcd(dx, dy)

                dx //= g
                dy //= g

                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy

                slopes[(dx, dy)] += 1

            for count in slopes.values():
                max_points = max(max_points, 1 + count)

        return max_points


        
        