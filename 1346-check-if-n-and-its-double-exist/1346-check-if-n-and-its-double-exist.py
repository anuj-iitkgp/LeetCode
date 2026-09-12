class Solution(object):
    def checkIfExist(self, arr):
        seen = set()
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False


        # for i in range(n):
        #     for j in range(n):
        #         if i != j and arr[i] == 2 * arr[j]:
        #             return True
        #             break
        # return False 
        