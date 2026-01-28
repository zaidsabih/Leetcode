class Solution(object):
    def pivotInteger(self, n):
        if n==1:
            return 1
        total=(n*(n+1))//2
        left=0
        for i in range(n):
            if left==total-left-i:
                return i
            left+=i
        return -1