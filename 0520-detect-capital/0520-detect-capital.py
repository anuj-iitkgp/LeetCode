class Solution(object):
    def detectCapitalUse(self, word):
        n = len(word)
        c = sum(1 for c in word if c.isupper())
        l = sum(1 for c in word if c.islower())
        l1 = sum(1 for c in word[1:] if c.islower())
        if c == n or l == n or (word[0].isupper() and l1 == n - 1):
            return True
        return False