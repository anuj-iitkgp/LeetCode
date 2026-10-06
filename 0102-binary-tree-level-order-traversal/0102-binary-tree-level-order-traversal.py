# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q = collections.deque([root])
        ans = []

        while q:
            l = len(q)
            curl = []
            for _ in range(l):
                node = q.popleft()
                curl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(curl)
        
        return ans