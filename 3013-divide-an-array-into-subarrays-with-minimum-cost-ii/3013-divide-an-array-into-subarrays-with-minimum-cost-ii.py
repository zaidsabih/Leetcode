class Solution(object):
    def minimumCost(self, nums, k, dist):
        from sortedcontainers import SortedList
        n = len(nums)
        if k == 1:
            return nums[0]
        small = SortedList()  # k-1 smallest
        large = SortedList()
        curr = 0
        # initial window: indices [1 .. dist+1]
        for i in range(1, min(n, dist + 2)):
            small.add((nums[i], i))
            curr += nums[i]
        # keep only k-1 smallest in `small`
        while len(small) > k - 1:
            v = small.pop()
            curr -= v[0]
            large.add(v)
        res = curr
        # sliding window
        for i in range(dist + 2, n):
            out = (nums[i - dist - 1], i - dist - 1)
            inn = (nums[i], i)
            # remove outgoing
            if out in small:
                small.remove(out)
                curr -= out[0]
                if large:
                    v = large.pop(0)
                    small.add(v)
                    curr += v[0]
            else:
                large.remove(out)
            # add incoming
            small.add(inn)
            curr += inn[0]
            if len(small) > k - 1:
                v = small.pop()
                curr -= v[0]
                large.add(v)
            res = min(res, curr)
        # add nums[0] (first subarray cost)
        return res + nums[0]