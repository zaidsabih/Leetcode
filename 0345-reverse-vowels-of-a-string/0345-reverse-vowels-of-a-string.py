class Solution(object):
    def reverseVowels(self, s):
        letters=list(s)
        i=0
        j=len(letters)-1
        vowels=set('aeiouAEIOU')
        while i<j:
            if  letters[i] not in vowels:
                i+=1
            elif letters[j] not in vowels:
                j-=1
            else:
                letters[i],letters[j]=letters[j],letters[i]
                i+=1
                j-=1
        return "".join(letters)