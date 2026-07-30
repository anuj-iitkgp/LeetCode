# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        
        if not root:
            return True
        
        left = self.heightOfTree(root.left)
        right = self.heightOfTree(root.right)
        
        
        if abs(left -  right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
        

    def heightOfTree(self, root):
        if not root:
            return 0

        return 1 + max(self.heightOfTree(root.left), self.heightOfTree(root.right))
