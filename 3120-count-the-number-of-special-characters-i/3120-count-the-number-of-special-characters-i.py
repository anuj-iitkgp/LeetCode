class Solution(object):
    def numberOfSpecialChars(self, word):
        l = set([x for x in word if x.islower()])
        u = set([x for x in word if x.isupper()])
        return sum(1 for c in l if c.upper() in u)