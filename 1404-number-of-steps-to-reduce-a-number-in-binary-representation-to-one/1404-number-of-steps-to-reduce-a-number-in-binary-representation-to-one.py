class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        base_10 = int(s,2)
        c=0
        while base_10 !=1:
            if base_10 %2==0:
                base_10//=2
            else:
                base_10+=1
            c+=1
        return c

        