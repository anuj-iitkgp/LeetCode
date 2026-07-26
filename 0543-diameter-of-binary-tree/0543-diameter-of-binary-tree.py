# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max_dia = 0

        # Removed 'self' parameter
        def depth(node):
            if not node:
                return 0
            
            # Call 'depth' directly instead of 'self.depth'
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Fixed typo: self.max_dia instead of self.max_dai
            self.max_dia = max(self.max_dia, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.max_dia