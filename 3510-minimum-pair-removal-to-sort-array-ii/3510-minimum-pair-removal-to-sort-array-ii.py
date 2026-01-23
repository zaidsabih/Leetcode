class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.append(float("inf"))
        left, right = list(range(-1, n)), list(range(1, n + 1))
        hp = [(nums[i] + nums[i + 1], i) for i in range(n - 1)]
        heapify(hp)
        ans = 0
        bad = sum([nums[i] > nums[i + 1] for i in range(n - 1)])
        while bad > 0:
            s, i = heappop(hp)
            r = right[i]
            if left[r] != i or nums[i] + nums[r] != s:
                continue
            rr = right[r]
            bad += (nums[left[i]] <= nums[i]) + (nums[i] <= nums[r]) + (nums[r] <= nums[rr])
            left[rr] = i
            right[i] = rr
            nums[i] = s

            bad -= 1 + (nums[left[i]] <= nums[i]) + (nums[i] <= nums[rr])
            if i > 0:
                heappush(hp, (nums[left[i]] + nums[i], left[i]))
            if rr < n:
                heappush(hp, (nums[i] + nums[rr], i))
            ans += 1
        return ans