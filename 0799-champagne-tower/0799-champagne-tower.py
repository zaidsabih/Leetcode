class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        tower = [[0.0] * (k + 1) for k in range(query_row + 2)]
        tower[0][0] = float(poured)
        
        for r in range(query_row + 1):
            for c in range(len(tower[r])):
                overflow = (tower[r][c] - 1.0) / 2.0
                if overflow > 0:
                    if r + 1 <= query_row:
                        tower[r + 1][c] += overflow
                        tower[r + 1][c + 1] += overflow
        
        return min(1.0, tower[query_row][query_glass])