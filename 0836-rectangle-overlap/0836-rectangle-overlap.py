class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        
        x1, y1 = rec1[0], rec1[1]
        x2, y2 = rec1[2], rec1[3]
        a1, b1 = rec2[0], rec2[1]
        a2, b2 = rec2[2], rec2[3]

        l = abs(x1 - x2) + abs(a1 - a2)
        h = abs(y1 - y2) + abs(b1 - b2)

        if abs(x1 - a2) >= l or abs(a1 - x2) >= l:
            return False
        if abs(y1 - b2) >= h or abs(b1 - y2) >= h:
            return False
        return True
         


        