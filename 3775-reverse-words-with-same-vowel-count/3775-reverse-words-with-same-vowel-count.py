class Solution(object):
    def reverseWords(self, s):
        def noOfVowels(k):
            return sum([1 for c in k if c in set(['a', 'e', 'i', 'o', 'u'])])
        words = s.split()
        t = noOfVowels(words[0])
        for i in range(1, len(words)):
            if noOfVowels(words[i]) == t:
                words[i] = words[i][::-1]
        return " ".join(word for word in words)
        