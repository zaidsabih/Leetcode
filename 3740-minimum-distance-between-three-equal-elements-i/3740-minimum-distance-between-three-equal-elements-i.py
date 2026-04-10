class Solution:
    def minimumDistance(self, nums):
        list_ = [[] for _ in range(len(nums))]

        for i in range(len(nums)):
            list_[nums[i] - 1].append(i)

        min_dist = float('inf')

        for indices in list_:
            if len(indices) >= 3:
                for t in range(2, len(indices)):
                    i = indices[t - 2]
                    k = indices[t]

                    min_dist = min(min_dist, 2 * (k - i))

        return -1 if min_dist == float('inf') else min_dist