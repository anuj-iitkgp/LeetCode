class Solution(object):
    def totalNumbers(self, digits):
        numSet = set()
        n = len(digits)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and k != i and digits[i] != 0:
                        x = 100 * digits[i] + 10 * digits[j] + digits[k]
                        if x % 2 == 0:
                            numSet.add(x)
        return len(numSet)