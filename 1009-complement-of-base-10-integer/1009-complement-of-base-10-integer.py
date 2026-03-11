class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 0

        n1 = 1
        while n1 <= n:
            n1 *= 2

        return n1 - 1 - n