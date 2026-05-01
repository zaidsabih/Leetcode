class Solution:
    def maxRotateFunction(self, nums):
        F = 0
        S = 0
        for i in range(len(nums)):
            F = F + (nums[i] * i)
            S = S + nums[i]

        max_val = F  # this is F0
        n = len(nums)
		
        for i in range(n - 1, 0, -1):
            F = F + S - n * nums[i]
            max_val = max(max_val, F)

        return max_val