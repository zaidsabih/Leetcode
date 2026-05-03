class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        new=s*2
        l=1
        r=len(s)
        while r<len(new):
            sub=new[l:r+1]
            if sub==goal:
                return True
            l+=1
            r+=1
        return False
        