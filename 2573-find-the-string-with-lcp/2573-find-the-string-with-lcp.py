class Solution(object):
    def findTheString(self, lcp):
        def nextChar():
            letter = ord('a') - 1
            while True:
                letter += 1
                yield chr(letter)

        n = len(lcp)
        res = []
        charGen = nextChar()
        for i in range(n):
            for j in range(i+1):
                if len(res) != i:
                    break

                if lcp[i][j]:
                    if j < i:
                        res.append(res[j])
                    else:
                        res.append( next(charGen) )

            if res and res[-1] > 'z':
                return ''

        def naiveCheck(i, j):
            val = 0
            iSize, jSize = n - i, n - j
            for k in range(min(iSize, jSize)):
                ik, jk = i + k, j + k
                if max(ik, jk) < len(res):
                    val += res[i+k] == res[j+k]
            if lcp[i][j] != val:
                return False
            return True

        def matrixCheck(i, j):
            val = 0
            # if out of the range of res, or the letters at i and j are the same, set to 1
            if i >= len(res) or j >= len(res) or res[j] == res[i]:
                val = 1
                ni, nj = i + 1, j + 1
                if max(ni, nj) < n:
                    val +=lcp[ni][nj]
            if val != lcp[i][j]:
                return False
            return True

        for i in range(n):
            for j in range(n):
                if not matrixCheck(i, j):
                    return ''
                    
        return ''.join(res)