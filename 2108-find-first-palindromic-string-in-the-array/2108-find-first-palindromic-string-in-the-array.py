class Solution(object):
    def firstPalindrome(self, words):
        def palindrome(word):
            i=0
            j=len(word)-1
            while i<=j:
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            return True
        for word in words:
            if palindrome(word):
                return word
        return ""

        