class Solution(object):
    def mySqrt(self, x):
        if x==0:
            return 0
        first=1
        last=x
        while first<=last:
            mid=first+(last-first)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                last=mid-1
            else:
                first=mid+1
        return last