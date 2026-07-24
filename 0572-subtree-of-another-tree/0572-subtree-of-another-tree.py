# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):



    def is_same_tree(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False
        
        if root1.val == root2.val:
            return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root1.right, root2.right) 
        return False

    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root and not subRoot:
            return True

        if not root or  not subRoot:
            return False
        
        if root.val == subRoot.val and self.is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        