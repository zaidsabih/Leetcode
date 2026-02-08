class Solution:
    def isBalanced(self, r):
        def f(n):
            if not n: return 0
            l,r = f(n.left),f(n.right)
            if abs(l-r)>1: raise
            return 1+max(l,r)

        try: f(r)
        except: return False
        else: return True