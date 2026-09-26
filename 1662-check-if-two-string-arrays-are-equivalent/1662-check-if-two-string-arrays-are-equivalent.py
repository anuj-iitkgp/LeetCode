class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        u, v = "".join(s for s in word1), "".join(s for s in word2)
        return u == v
        