class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        
        if m > n:
            return self.maxDotProduct(nums2, nums1)
            
        dp = [float('-inf')] * (m + 1)
        
        for i in range(1, n + 1):
            prev_diag = float('-inf')
            
            for j in range(1, m + 1):
                curr_product = nums1[i-1] * nums2[j-1]
                
                temp = dp[j]
                
                dp[j] = max(
                    curr_product,               
                    curr_product + prev_diag,   
                    dp[j],                       
                    dp[j-1]                      
                )
                
                prev_diag = temp

        return dp[m]