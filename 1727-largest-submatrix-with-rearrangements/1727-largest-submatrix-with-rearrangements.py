#translated using AI
class Solution:
    def largestSubmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]

        for i in range(m):
            arr = sorted(matrix[i])

            for j in range(n):
                height = arr[j]
                width = n - j
                ans = max(ans, height * width)

        return ans