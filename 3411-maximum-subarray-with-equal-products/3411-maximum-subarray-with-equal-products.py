class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def gcdArr(arr):
            res = arr[0]
            for i in range(1, len(arr)):
                res = gcd(res, arr[i])
            return res
        
        def lcm(a,b):
            return (a * b) // gcd(a, b)
        
        def lcmArr(arr):
            res = arr[0]
            for i in range(1, len(arr)):
                res = lcm(res, arr[i])
            return res
        
        
        def prod(arr):
            k = len(arr)
            p = 1
            for i in range(k):
                p *= arr[i]
            return p
        
        l = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if prod(nums[i:j+1]) == lcmArr(nums[i:j+1]) * gcdArr(nums[i:j+1]):
                    l = max(l, j - i + 1)
        return l


        