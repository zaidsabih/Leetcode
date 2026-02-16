class Solution(object):
    def reverseBits(self, n):
        ans = 0
        
        for _ in range(32):
            ans <<= 1          # make space
            ans |= (n & 1)     # copy last bit
            n >>= 1            # remove last bit
        
        return ans