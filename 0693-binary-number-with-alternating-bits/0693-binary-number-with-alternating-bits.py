class Solution:
    def hasAlternatingBits(self, n):
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0