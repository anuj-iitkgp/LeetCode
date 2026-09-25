class Solution(object):
    def sumAndMultiply(self, n):
        if n == 0:
            return 0
        def digitSum(n):
            t = 0
            while n:
                t += n % 10
                n //= 10
            return t
        x = digitSum(n)
        m = "".join(s for s in str(n) if s != "0" )
        return x * int(m)
        