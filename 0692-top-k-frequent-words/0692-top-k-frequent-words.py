from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        sorted_count = sorted(count.keys(), key=lambda w: (-count[w], w))

        return sorted_count[:k]