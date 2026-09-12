class Solution(object):
    def checkIfExist(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
                    break
        return False 
        