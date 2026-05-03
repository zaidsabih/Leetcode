class Solution(object):
    def rotatedDigits(self, n):
        d={"0":"0","1":"1","8":"8","2":"5","5":"2","6":"9","9":"6"};
        res=0;
        for i in range(1,n+1):
            s=str(i);
            flag=1;
            t=""
            for j in s:
                if(j not in d):
                    flag=0;
                    break;
                else:
                    t+=d[j];
            if(flag==0):
                continue;
            if(int(t)!=i):
                res+=1;
        return res



        """
        :type n: int
        :rtype: int
        """
        