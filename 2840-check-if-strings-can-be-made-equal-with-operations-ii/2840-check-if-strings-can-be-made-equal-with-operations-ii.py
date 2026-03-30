class Solution:
    def checkStrings(self, s1, s2):
        freq = [0] * 52
        for i in range(len(s1)):
            off = (i & 1) * 26
            freq[ord(s1[i]) - ord('a') + off] += 1
            freq[ord(s2[i]) - ord('a') + off] -= 1
        return all(f == 0 for f in freq)