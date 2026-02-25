class Solution(object):
    def sortByBits(self, arr):
        d={};
        for i in arr:
            b=bin(i)[2:].count("1");
            if(b in d):
                d[b].append(i);
            else:
                d[b]=[i]
        res=[];
        for i in sorted(d):
            res.extend(sorted(d[i]));
        return res
        """
        :type arr: List[int]
        :rtype: List[int]
        """