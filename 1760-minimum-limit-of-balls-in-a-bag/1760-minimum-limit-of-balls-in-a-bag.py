class Solution(object):
    def minimumSize(self, nums, maxOperations):
        def ispossible(mid):
            operations=0
            for i in nums:
                operations+=(i-1)//mid
                if operations>maxOperations:
                    return False
            return True
        left=1
        right=max(nums)
        ans=right
        while left<=right:
            mid=left+(right-left)//2
            if ispossible(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans

        