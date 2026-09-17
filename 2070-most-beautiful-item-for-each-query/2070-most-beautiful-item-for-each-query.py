class Solution(object):
    def maximumBeauty(self, items, queries):

        items.sort(key = lambda x: x[0])
        

        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])
            
        ans = []
        n = len(items)
        

        def binary_search(q):
            left, right = 0, n - 1
            best_idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                if items[mid][0] <= q:
                    best_idx = mid   
                    left = mid + 1
                else:
                    right = mid - 1  
                    
            return items[best_idx][1] if best_idx != -1 else 0

        for q in queries:
            ans.append(binary_search(q))
            
        return ans