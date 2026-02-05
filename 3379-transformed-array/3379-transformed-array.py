class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = nums[(i + nums[i]) % n]
        return ans