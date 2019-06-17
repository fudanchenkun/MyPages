import sys
MAXINT = sys.maxint
MININT = -sys.maxint-1


"""

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (m + n + 1) - 1 # 合并填充后的中位数位置 (A[k] + A[k+1])/2
        c1 = m # nums1的cut位置
        c2 = k - m # nums2的cut位置
        lo = 0
        hi = 2*m
        l1max, r1min, l2max, r2min = 0, 0, 0, 0
        while lo <= hi:
            c1 = (lo + hi) / 2
            c2 = k - c1
            l1max = nums1[(c1-1)/2] if c1 > 0 else MININT
            r1min = nums1[c1/2] if c1 != 2*m else MAXINT
            l2max = nums2[(c2-1)/2] if c2 > 0 else MININT
            r2min = nums2[c2/2] if c2 != 2*n else MAXINT

            if l1max > r2min:
                hi = c1 - 1
            elif l2max > r1min:
                lo = c1 + 1
            else:
                break

        return (max(l1max, l2max)+min(r1min, r2min)) / 2.0

