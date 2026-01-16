class Solution(object):
    def reverse(self, x):
        is_negative=False
        if x<0:
            is_negative=True
            x*=-1
        reverse=0
        while x>0:
            last=x%10
            reverse=reverse*10+last
            x//=10
        if reverse>2**31 -1:
            return 0
        
        return reverse*-1 if is_negative else reverse
        