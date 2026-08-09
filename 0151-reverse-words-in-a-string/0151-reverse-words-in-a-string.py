class Solution(object):

  def reverseWords(self, s):
    
    # Recursion
    s1 = s.split()
    def reverse(l, r):
        if l < r:
            reverse(l + 1, r - 1)
            s1[l], s1[r] = s1[r], s1[l]

    reverse(0, len(s1) - 1)
    return " ".join(s1)

# Time and Space: O(n)
        