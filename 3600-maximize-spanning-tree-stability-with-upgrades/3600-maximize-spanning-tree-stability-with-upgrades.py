class Solution(object):

    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def unite(self, a, b):
            ra = self.find(a)
            rb = self.find(b)

            if ra == rb:
                return False

            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra

            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True

    def check(self, X, n, edges, k):
        dsu = self.DSU(n)
        comps = n

        for e in edges:
            if e[3] == 1:
                if e[2] < X:
                    return False
                if dsu.unite(e[0], e[1]):
                    comps -= 1

        for e in edges:
            if e[3] == 0 and e[2] >= X:
                if dsu.unite(e[0], e[1]):
                    comps -= 1

        if comps - 1 > k:
            return False

        for e in edges:
            if e[3] == 0 and e[2] < X and 2 * e[2] >= X:
                if dsu.unite(e[0], e[1]):
                    comps -= 1

        return comps == 1

    def maxStability(self, n, edges, k):

        init = self.DSU(n)
        max_must = 2 * 10**9

        for e in edges:
            if e[3] == 1:
                if not init.unite(e[0], e[1]):
                    return -1
                max_must = min(max_must, e[2])

        full = self.DSU(n)
        comps = n

        for e in edges:
            if full.unite(e[0], e[1]):
                comps -= 1

        if comps > 1:
            return -1

        low = 1
        high = min(2 * 10**5, max_must)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if self.check(mid, n, edges, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans