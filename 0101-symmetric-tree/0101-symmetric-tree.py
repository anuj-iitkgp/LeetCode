class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        q = deque([(root.left, root.right)])

        while q:
            t1, t2 = q.popleft()

            if not t1 and not t2:
                continue
            
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            # add mirror pairs to queue
            q.append((t1.left, t2.right))
            q.append((t1.right, t2.left))
        return True