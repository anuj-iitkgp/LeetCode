class Solution(object):
    def findComplement(self, num):
        
        a = (1 << num.bit_length()) - 1
        return a ^ num
        
        

        