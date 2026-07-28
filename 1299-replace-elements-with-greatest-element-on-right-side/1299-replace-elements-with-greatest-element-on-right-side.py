class Solution(object):
    def replaceElements(self, arr):
        # if len(arr) == 1:
        #     return [-1]
        
        # for i in range(len(arr) ):
        #     maxi = float("-inf")
        #     for j in range(i + 1, len(arr)):
        #         if maxi < arr[j]:
        #             maxi = max(maxi, arr[j])
        #             arr[i] = maxi
        #     if i == len(arr) - 1:
        #         arr[i] = -1
        # return arr   

        # T.C> = O(n^2)    

        maxi = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = maxi
            maxi = max(maxi, curr)
        return arr




