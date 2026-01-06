class Solution(object):
    def isPalindrome(self, s):
        lst="".join(ch for ch in s if ch.isalnum())
        lst=list(lst.lower())
        i=0
        j=len(lst)-1
        while i<j:
            if lst[i]==lst[j]:
                i+=1
                j-=1
            else:
                return False
        return True