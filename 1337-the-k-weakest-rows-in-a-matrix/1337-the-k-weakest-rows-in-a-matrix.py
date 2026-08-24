from collections import Counter
class Solution(object):
    def kWeakestRows(self, mat, k):
        
        n = len(mat)
        ans = []
        for i in range(n):
            ans.append([i,sum(mat[i])])

        ans.sort(key = lambda x : x[1])
        res = []
        for i in range(len(ans)):
            res.append(ans[i][0])
        return res[:k]

        
        
        
        
        
        