class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        ans = 0
        
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ans = max(ans, j - i)
            i = j
        
        for x, y in (('a','b'), ('a','c'), ('b','c')):
            diff = 0
            first = {0: -1}
            start = -1
            for i, ch in enumerate(s):
                if ch != x and ch != y:
                    diff = 0
                    first = {0: i}
                    start = i
                    continue
                diff += 1 if ch == x else -1
                if diff in first:
                    ans = max(ans, i - first[diff])
                else:
                    first[diff] = i
        
        a = b = c = 0
        first = {(0, 0): -1}
        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            key = (b - a, c - a)
            if key in first:
                ans = max(ans, i - first[key])
            else:
                first[key] = i
        
        return ans