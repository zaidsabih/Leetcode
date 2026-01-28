class Solution(object):
    def minCost(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        n,m = len(grid),len(grid[0])
        cost = [[float("inf") for _ in range(m)] for _ in range(n)]
        points = [(i,j) for i in range(n) for j in range(m)]
        points.sort(key = lambda p: grid[p[0]][p[1]])
        points_val_lastidx= {}
        for i in range(len(points)):
            x,y = points[i]
            val =  grid[x][y]
            points_val_lastidx[val] = i

        for t in range(k+1):
            minCost = float("inf")
            start = 0
            for i in range(len(points)):
                x,y = points[i]
                val = grid[x][y]
                minCost = min(minCost,cost[x][y])
                if i!=points_val_lastidx[val]:
                    continue
                for k in range(start,i+1):
                    kx,ky = points[k]
                    cost[kx][ky] = minCost
                start = i+1
            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    if i==n-1 and j ==m-1:
                        cost[i][j] = 0
                        continue
                    if j!=m-1:
                        cost[i][j] = min(cost[i][j],cost[i][j+1]+grid[i][j+1])
                    if i!=n-1:
                        cost[i][j] = min(cost[i][j],cost[i+1][j]+grid[i+1][j])
        return cost[0][0]

        