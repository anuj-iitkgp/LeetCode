class Solution(object):
    def maxProduct(self, n):
        first_max = float('-inf')
        second_max = float('-inf')
        while n:
            i = n % 10
            n //= 10

            if first_max < i:
                second_max = first_max
                first_max = i
            elif second_max < i:
                second_max = i
        return first_max * second_max