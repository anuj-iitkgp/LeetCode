# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        # if not root:
        #     return TreeNode(val)
        
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)
        # else:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root

        new_node = TreeNode(val)
        
        if not root:
            return new_node

        curr = root

        while True:
            if curr.val > val:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left
            elif curr.val < val:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right
            else:
                break
                
        return root