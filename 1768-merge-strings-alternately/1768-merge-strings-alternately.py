class Solution(object):
    def mergeAlternately(self, word1, word2):
        answer=[]
        word1=list(word1)
        word2=list(word2)
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            answer.append(word1[i])
            i+=1
            answer.append(word2[j])
            j+=1
        while j<len(word2):
            answer.append(word2[j])
            j+=1
        while i<len(word1):
            answer.append(word1[i])
            i+=1
        return "".join(answer)