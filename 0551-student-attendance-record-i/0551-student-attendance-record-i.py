class Solution(object):
    def checkRecord(self, s):
        a = 0
        l = 0 
        n = len(s)
        for i in range(n):
            if s[i] == 'A':
                a += 1
                if a >= 2:
                    return False
            
        for i in range(2, n):
            if s[i - 2] == 'L'and s[i - 1] == 'L' and s[i] == 'L':
                return False
        return True

                