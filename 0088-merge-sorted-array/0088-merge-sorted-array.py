class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k=m+n-1
        i=m-1
        j=n-1
        while  j>=0 and i>=0:
            if nums2[j]>=nums1[i]:
                nums1[k]=nums2[j]
                j-=1
            elif nums1[i]>=nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
            
        return nums1
