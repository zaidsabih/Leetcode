class Solution:
    def closestTarget(self, words, target, s):
        n = len(words)
        for i in range((n >> 1) + 1):
            if ((words[(s + i) % n] == target) |
                (words[(s - i) % n] == target)):
                return i
        return -1