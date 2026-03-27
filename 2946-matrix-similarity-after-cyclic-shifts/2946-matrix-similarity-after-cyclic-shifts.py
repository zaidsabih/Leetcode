class Solution:
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])
        shifts = k % n

        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    newCol = (j - shifts + n) % n 
                else:
                    newCol = (j + shifts) % n
                
                if mat[i][j] != mat[i][newCol]:
                    return False
        
        return True