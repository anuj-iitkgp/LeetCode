from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):

        res = []

        def dfs(node, depth):
            if not node:
                return
# Start a new level array if visiting this depth for the first time
            if depth == len(res):
                res.append([])
# Odd levels(0-idx) append to left, even levels append to right

            if depth % 2 == 0:
                res[depth].append(node.val)
            else:
                res[depth].insert(0, node.val) # prepend for right to left order
            
            # traverse left then right

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res

