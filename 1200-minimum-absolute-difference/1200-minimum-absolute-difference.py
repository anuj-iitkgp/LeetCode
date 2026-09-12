class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        minDif = abs(arr[0] - arr[1] )
        ans = []
        n = len(arr)

        for i in range(1, n - 1):
            minDif = min(minDif, abs(arr[i + 1] - arr[i]))
        
        for i in range(n - 1):
            if minDif == abs(arr[i + 1] - arr[i]):
                ans.append([arr[i], arr[i + 1]])
        return ans



        