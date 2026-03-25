class Solution(object):
    def canPartitionGrid(self, grid):
        n = len(grid)
        m = len(grid[0])

        def checkHz():
            st = set()
            pref = 0

            for i in range(n):
                rowSum = 0
                for j in range(m):
                    rowSum += grid[i][j]
                pref += rowSum
                st.add(pref)

            if pref % 2 != 0:
                return False

            return (pref // 2) in st

        def checkVz():
            st = set()
            pref = 0

            for j in range(m):
                colSum = 0
                for i in range(n):
                    colSum += grid[i][j]
                pref += colSum
                st.add(pref)

            if pref % 2 != 0:
                return False

            return (pref // 2) in st

        return checkHz() or checkVz()