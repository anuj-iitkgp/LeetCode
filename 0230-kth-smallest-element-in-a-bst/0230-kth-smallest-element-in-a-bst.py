# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
    

        def inorderTraversal(root):
            if not root:
                return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
        
        val = inorderTraversal(root)
        return val[k - 1]
            
