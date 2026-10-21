class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        tot = min(x, y//4)
        if tot & 1:
            return "Alice"
        return "Bob"