class Solution(object):
    def checkString(self, s):
        n = len(s)
        for i in range(n - 1):
            if s[i] == 'b' and s[i + 1] == 'a':
                return False
        return True
        