class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next
        index = 1
        
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')

        while curr and curr.next:
            val = curr.val
            p_val = prev.val
            n_val = curr.next.val
            
            # Check for local maxima or minima
            if (p_val < val > n_val) or (p_val > val < n_val):
                if first_cp == -1:
                    first_cp = index
                else:
                    dist = index - prev_cp
                    if dist < min_dist:
                        min_dist = dist
                prev_cp = index

            prev = curr
            curr = curr.next
            index += 1

        if first_cp == -1 or prev_cp == first_cp:
            return [-1, -1]

        return [min_dist, prev_cp - first_cp]