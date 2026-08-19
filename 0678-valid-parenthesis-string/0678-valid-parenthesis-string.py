from collections import Counter
class Solution(object):
    def checkValidString(self, s):
        low = 0 # min required '('
        high = 0 # max possible '('

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low = max(0, low - 1)
                high -= 1
            else: # char '*""
                low = max(0, low - 1) # '*' treated as ')'
                high += 1 # '*' treated as ')'
            # If high < 0, we have too many ')' that cannot be matched
            if high < 0:
                return False
            # If low == 0, all '(' can be properly matched
        return low == 0

# Time Complexity: O(n)
# Space Complexity: O(1)