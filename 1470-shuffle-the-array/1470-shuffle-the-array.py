class Solution(object):
    def shuffle(self, nums, n):
        answer=[]
        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i+n])
        return answer