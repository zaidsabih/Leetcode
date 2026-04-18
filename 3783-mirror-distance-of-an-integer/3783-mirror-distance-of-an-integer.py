class Solution:
    def mirrorDistance(self, n):
        # Convert to string, reverse it, convert back to int, and find the absolute difference
        reversed_n = int(str(n)[::-1])
        return abs(n - reversed_n)