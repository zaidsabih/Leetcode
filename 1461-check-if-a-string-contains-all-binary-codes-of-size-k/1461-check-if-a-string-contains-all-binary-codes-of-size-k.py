class Solution:
    def hasAllCodes(self, s, k):
        seen = set()

        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])

        return len(seen) == (1 << k)