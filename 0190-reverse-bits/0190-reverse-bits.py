class Solution(object):
    def reverseBits(self, n):
        
        binar = (bin(n)[2:]).zfill(32)
        rev_binar = binar[::-1]
        decimal = int(rev_binar, 2)
        return decimal
        

        