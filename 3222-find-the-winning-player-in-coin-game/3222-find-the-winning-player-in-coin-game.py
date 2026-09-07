class Solution(object):
    def winningPlayer(self, x, y):

        if (min(x, y // 4)) % 2 != 0:
            return "Alice"
        return "Bob"