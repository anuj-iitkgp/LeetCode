class Solution(object):
    def addBinary(self, a, b):
        ans = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(a[i]) - 48  
                i -= 1
            if j >= 0:
                carry += ord(b[j]) - 48
                j -= 1
            
            ans.append(str(carry & 1))
            carry >>= 1

        return "".join(reversed(ans))