class Solution(object):
    def maxAlternatingSum(self, nums):
        arr = [abs(x) for x in nums]
        n, ans = len(arr), 0
        i, j = 0, n - 1
        arr.sort()
        print(arr)

        if n % 2 != 0:
            ans += arr[n // 2]* arr[n // 2]
        while i < j:
            ans += arr[j] * arr[j]
            ans -= arr[i] * arr[i]
            i += 1
            j -= 1
        return ans