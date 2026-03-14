class Solution:
    def getHappyString(self, n, k):
        r = ['']
        for _ in range(n):
            r = [s+c for s in r for c in 'abc' if s[-1:]!=c]

        return ''.join(r[k-1:k])