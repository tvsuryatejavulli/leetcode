from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1+=nums2
        nums1.sort()
        n=len(nums1)
        if n%2==1:
            return float(format(nums1[n//2],".5f"))
        else:
            return float(format((nums1[n//2 - 1]+nums1[n//2 ])/2.0,"5f"))
        