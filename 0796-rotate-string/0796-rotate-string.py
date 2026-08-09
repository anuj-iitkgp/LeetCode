class Solution(object):
    def rotateString(self, s, goal):
        
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if goal == rotated:
                return True
        return False

# Time Complexity: O(N^2) since generating N rotations and each comparison takes O(N) time.

# Space Complexity: O(N) for the space needed to store each rotated string.