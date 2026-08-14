class Solution(object):
    def xorOperation(self, n, start):
        xor_all = 0
        for i in range(n):
            xor_all ^= start + 2 * i
        return xor_all