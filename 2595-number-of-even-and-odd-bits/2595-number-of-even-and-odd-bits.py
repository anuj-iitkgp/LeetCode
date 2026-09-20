class Solution(object):
    def evenOddBit(self, n):
        nBin = bin(n)[2:][::-1]
        odd, even = 0, 0 
        for i in range(len(nBin)):
            if nBin[i] == '1' and i % 2 != 0:
                odd += 1
            if nBin[i] == '1' and i % 2 == 0:
                even += 1
        return [even, odd]
        