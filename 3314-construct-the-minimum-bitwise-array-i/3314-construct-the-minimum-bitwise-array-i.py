class Solution(object):
    def minBitwiseArray(self, A):
        res = []
        for a in A:
            if a % 2 == 0:
                res.append(-1)
            else:
                res.append(a - ((a + 1) & (-a - 1)) // 2)
        return res