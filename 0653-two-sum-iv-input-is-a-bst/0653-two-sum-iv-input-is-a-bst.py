# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):

# First approach: inorder + 2 sum problem

        # if not root:
        #     return True
        
            
        # def inorder(root):
        #     if not root:
        #         return []
        #     return inorder(root.left) + [root.val] + inorder(root.right)
        
        # val = inorder(root)
        # l = 0
        # r = len(val) - 1

        # while l < r:
        #     sum = val[l] + val[r]
        #     if sum < k:
        #         l += 1
        #     elif sum > k:
        #         r -= 1
        #     else:
        #         return True
        
        # return False

#   2nd approach using hashset

        seen = set()

        def dfs(root):
            if not root:
                return False
            
            if (k - root.val) in seen:
                return True
            seen.add(root.val)
            return dfs(root.left) or dfs(root.right)
        return dfs(root)