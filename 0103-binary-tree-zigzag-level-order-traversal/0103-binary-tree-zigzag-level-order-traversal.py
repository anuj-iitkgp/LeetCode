from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res = []
        q = deque([root])
        left_to_right = True

        while q:
            level_size = len(q)
            current_level = deque()

            for _ in range(level_size):
                node = q.popleft()

                # Alternate direction of insertion for the current level
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)

                # Push child nodes for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(list(current_level))
            left_to_right = not left_to_right  # Flip direction for next level

        return res