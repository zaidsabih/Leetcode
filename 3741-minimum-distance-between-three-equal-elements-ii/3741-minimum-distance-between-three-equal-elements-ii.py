class Solution(object):
    def minimumDistance(self, n):
        h={}
        l=[]
        for i in range(len(n)):
            if str(n[i]) not in h:
                h[str(n[i])]=[]
            h[str(n[i])].append(i)
        for i in h.values():
            if len(i)>=3:
                l.append(i)
        k=[]
        for i in range(len(l)):
            if len(l[i])>3:
                for j in range(0,len(l[i])-2):
                    x=l[i][j]
                    y=l[i][j+1]
                    z=l[i][j+2]
                    k.append(2*(max(x,y,z)-min(x,y,z)))
            else:
                x=l[i][0]
                y=l[i][1]
                z=l[i][2]
                k.append(2*(max(x,y,z)-min(x,y,z)))

        if len(k)==0:
            return -1
        else:
            return min(k)

        