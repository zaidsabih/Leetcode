class Solution(object):
    def isPalindrome(self, x):
        reverse=0
        shallow_copy=x
        while x>0:
            last=x%10
            reverse=reverse*10+last
            x//=10
        return reverse==shallow_copy