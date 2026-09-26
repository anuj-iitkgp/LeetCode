class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        for i, w in enumerate(words, start = 1):
            if w.startswith(searchWord):
                return i
        return -1
        