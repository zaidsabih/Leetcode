class Solution:
    def minBitwiseArray(self, nums):
        for i in range(len(nums)):
            num = nums[i]
            r = -1
            d = 1
            while num & d:
                r = num - d
                d <<= 1
            nums[i] = r
        return nums