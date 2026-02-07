class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=count=0
        for c in s:
            if c=='b':
                count+=1
            elif count:
                res+=1
                count-=1
        return res