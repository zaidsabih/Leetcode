class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        z = s.count('0')

        if z == 0:
            return 0

        t = (z + k - 1) // k

        while True:
            tk = t * k

            if tk >= z and (tk - z) % 2 == 0:
                if t % 2 == 0:
                    if tk <= t * n - z:
                        return t
                else:
                    if tk <= (t - 1) * n + z:
                        return t

        
            if t > 2 * n:
                return -1

            t += 1