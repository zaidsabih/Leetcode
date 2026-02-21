class Solution:
    def countPrimeSetBits(self, left, right):
        mask = 665772
        ans = 0

        for i in range(left, right + 1):
            bits = self.countBits(i)

            if ((mask >> bits) & 1) == 1:
                ans += 1

        return ans

    def countBits(self, n):
        c = 0
        while n > 0:
            if n & 1:
                c += 1
            n >>= 1
        return c