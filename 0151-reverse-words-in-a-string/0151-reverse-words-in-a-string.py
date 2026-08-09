class Solution(object):

  def reverseWords(self, s):
    # 1. Split the string into words (handles extra spaces automatically)
    words = s.split()

    tmp = []
    # 2. Iterate backwards through the list of words
    for i in range(len(words) - 1, -1, -1):
      tmp.append(words[i])

    # 3. Join the words back together with a single space and return
    return " ".join(tmp)


# Time and Space: O(n)
        