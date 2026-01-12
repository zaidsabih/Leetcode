class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0
        
        for i in xrange(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            
            total_time += max(abs(x2 - x1), abs(y2 - y1))
            
        return total_time