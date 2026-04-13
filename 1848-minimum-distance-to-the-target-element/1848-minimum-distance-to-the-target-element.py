class Solution:
    def getMinDistance(self, nums, target, start):

        result = len(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                result = min(result, abs(i - start))

        return result