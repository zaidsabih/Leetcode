class Solution(object):
    def reversePrefix(self, word, ch):
        ans1=[]
        ans2=[]
        c=0
        for i in list(word):
            if i==ch:
                ans1.append(i)
                c+=1
                break
            else:
                ans1.append(i)
                c+=1
        for i in range(c,len(word)):
            ans2.append(word[i])
        if ch not in word:
            return word
        i=0
        j=len(ans1)-1
        while i<j:
            ans1[i],ans1[j]=ans1[j],ans1[i]
            i+=1
            j-=1
        return "".join(ans1)+"".join(ans2)
            
            

        