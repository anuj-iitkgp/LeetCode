class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        def calHeight(c1, c2):
            b = int((c1)**(0.5))
            r = int((-1 + (1 + 4 * c2)**(0.5)) // 2)
            
            if b > r:
                return 2 * r + 1
            else:
                return 2 * b
        a = max(calHeight(red, blue), calHeight(blue, red))
        return a
                