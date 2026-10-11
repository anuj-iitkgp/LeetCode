class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26
class Solution(object):
    def checkIfPangram(self, sentence):
        s = set(sentence)
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for char in characters:
            if char not in s:
                return False
        return True
        