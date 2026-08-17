class Solution(object):

  def rightSideView(self, root):
    res = []

    def dfs(node, depth):
      if not node:
        return

      # First time visiting this depth level
      if depth == len(res):
        res.append(node.val)

      # Prioritize right side first
      dfs(node.right, depth + 1)
      dfs(node.left, depth + 1)

    dfs(root, 0)
    return res