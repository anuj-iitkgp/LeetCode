# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        
        if not preorder or not inorder:
            return None
        # root is always the first element of preorder

        root_val = preorder[0]
        root = TreeNode(root_val)

        #find index of root in inorder traversal
        mid = inorder.index(root_val)

        # recursively construct left and right subtree

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid+ 1:])

        return root

