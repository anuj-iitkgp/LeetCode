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
            nxt = curr.next
            
            # Check if curr is a local maxima or local minima
            is_maxima = prev.val < curr.val and curr.val > nxt.val
            is_minima = prev.val > curr.val and curr.val < nxt.val

            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = index
                else:
                    # Update minimum distance between adjacent critical points
                    min_dist = min(min_dist, index - prev_cp)
                
                prev_cp = index

            prev = curr
            curr = curr.next
            index += 1

        # Return [-1, -1] if fewer than 2 critical points were found
        if first_cp == -1 or prev_cp == first_cp:
            return [-1, -1]

        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]