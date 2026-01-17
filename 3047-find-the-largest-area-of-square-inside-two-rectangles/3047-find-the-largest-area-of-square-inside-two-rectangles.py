class Solution:
    def largestSquareArea(self, a, b):
        return max(0,max(min(min(x2,i2)-max(x1,i1),min(y2,j2)-max(y1,j1))
            for ((x1,y1),(x2,y2)),((i1,j1),(i2,j2)) in combinations(zip(a,b),2)))**2