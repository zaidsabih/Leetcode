class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n_cols = len(matrix[0])
        heights = [0] * (n_cols + 1) 
        max_area = 0
        for row in matrix:
            for i in range(n_cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area