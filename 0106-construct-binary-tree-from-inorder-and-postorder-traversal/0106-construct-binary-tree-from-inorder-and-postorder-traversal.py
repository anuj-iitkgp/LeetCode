# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        # Root value is the last element of postorder
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Index of root in inorder traversal
        mid = inorder.index(root_val)

        # Build left and right subtrees
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])

        return root