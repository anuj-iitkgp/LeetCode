class Solution(object):
    def xorOperation(self, n, start):

        nums = [0] * n
        for i in range(n):
            nums[i] = start + 2 * i

        xor_all = 0
        for i in range(n):
            xor_all ^= nums[i]
        return xor_all