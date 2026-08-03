# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
# first approach inorder + compare with origin and swap thwm

        # self.temp = []

        # def inorder(node):
        #     if not node:
        #         return
            
        #     inorder(node.left)
        #     self.temp.append(node)
        #     inorder(node.right)
        # inorder(root)

        # srt = sorted(n.val for n in self.temp)
        # print(srt)
        # for i in range(len(srt)):
        #     self.temp[i].val = srt[i]


        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            # Detect where the BST order is violated

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev # First node is from the 1st drop
                self.second = node # Second node updates on 1st drop (adjacent) & 2nd drop (non-adjacent)
            
            self.prev = node

            inorder(node.right)
        inorder(root)
        # Swap the values back
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val


    