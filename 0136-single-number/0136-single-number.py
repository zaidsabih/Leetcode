class Solution(object):
    def singleNumber(self, nums):
        count=0
        for num in nums:
            count^=num
        return count