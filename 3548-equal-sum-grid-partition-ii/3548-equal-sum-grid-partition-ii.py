class Solution:
    def canPartitionGrid(self, grid):
        def check(g):
            m, n = len(g), len(g[0])
            total = sum(sum(row) for row in g)
            prefix = 0
            seen = {0}
            for i in range(m):
                prefix += sum(g[i])
                target = 2 * prefix - total
                # first row: only ends
                if i == 0:
                    if target in (0, g[0][0], g[0][-1]):
                        return True
                # single column: only top or current row
                elif n == 1:
                    if target in (0, g[0][0], g[i][0]):
                        return True
                else:
                    if target in seen:
                        return True
                # add all elements of current row to seen
                for val in g[i]:
                    seen.add(val)
            return False

        # rotate 4 times
        def rotate(g):
            return [list(row) for row in zip(*g[::-1])]

        for _ in range(4):
            if check(grid):
                return True
            grid = rotate(grid)
        return False