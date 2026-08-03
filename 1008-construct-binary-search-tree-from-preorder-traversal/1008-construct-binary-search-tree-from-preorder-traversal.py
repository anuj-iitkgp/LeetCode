# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        if not preorder:
            return []
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        for val in preorder[1:]:
            self.insertBST(root, val)
        return root

    def insertBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            root.right = self.insertBST(root.right, val)
        else:
            root.left = self.insertBST(root.left, val)
        return root


        
        
        

    

        
 