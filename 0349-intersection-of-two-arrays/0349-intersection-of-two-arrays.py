class Solution(object):
    def intersection(self, nums1, nums2):
        union=set()
        for i in nums1:
            if i in nums2:
                union.add(i)
        for j in nums2:
            if j in nums1:
                union.add(j)
        return list(union)


            

        