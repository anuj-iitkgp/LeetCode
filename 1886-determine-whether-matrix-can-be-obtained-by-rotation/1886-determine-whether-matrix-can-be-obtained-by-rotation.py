class Solution(object):
    def findRotation(self, mat, target):
        # Check up to 4 rotations (0, 90, 180, 270 degrees)
        for _ in range(4):
            if mat == target:
                return True
            
            # Rotate 90 degrees clockwise
            mat = [list(row) for row in zip(*mat)]
            for i in range(len(mat)):
                mat[i] = mat[i][::-1]
                
        return False