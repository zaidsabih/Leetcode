class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        max_size = 0
        sums = []
        
        #iterate over each cell, we also need to take account of each cell value and append it to sum as rhombus can be of size 0
        for i in range(m):
            for j in range(n):
            # assume you are in cell (1, 2) in 5x5 matrix, and it is centre of rhombus, how many steps can you take up, left, bottom, right
            #top = you can take a 1 step
            #left = j
            # bottom = total  rows - 1 - i
            # right = total coumns - 1 - j
            # for any center you can get the min size out of which you are out of bounds.
                max_size = min(i, m-1-i, j, n-1-j)
                # if 0 that means you cannot form a rhombus so we append the sum of that cell.
                if max_size == 0:
                    sums.append(grid[i][j])
                else:
                # if max_size is greater than 1, then there is a possibility of 1 rhombus and we need to find the sum of all the edges in the rhombus.
                    for s in range(0, max_size+1):
                        if s == 0:
                            sums.append(grid[i][j]) 
                        else:
                        # calculate the top corner for each size if size is 1 then we have four corners if size is 2, then we have 8 corners           
                            r, c = i - s, j
                            rhombus_sum = 0
                            # iterate from top to left
                            for step in range(s):
                                rhombus_sum += grid[r][c]
                                r += 1
                                c -= 1
                            # iterate from left to bottom
                            for step in range(s):
                                rhombus_sum += grid[r][c]
                                r += 1
                                c += 1
                            # iterate from bottom to left
                            for step in range(s):
                                rhombus_sum += grid[r][c]
                                r -=1
                                c +=1
                            # iterate from left to top
                            for step in range(s):
                                rhombus_sum += grid[r][c]
                                r -= 1
                                c -=1
                            sums.append(rhombus_sum)
        # distinct sum arrange in descending order
        unique_sum = sorted(list(set(sums)), reverse=True)
        return unique_sum[0:3]

        