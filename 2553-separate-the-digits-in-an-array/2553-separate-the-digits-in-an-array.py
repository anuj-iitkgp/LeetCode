class Solution(object):
    def separateDigits(self, nums):
        # res = []
        # for num in nums:
        #     for digit in str(num):
        #         res.append(int(digit))
        # return res

        res = []
        for num in nums:
            digit = []
            while num > 0:
                digit.append(num % 10)
                num //= 10
            res.extend(digit[::-1])
        return res

