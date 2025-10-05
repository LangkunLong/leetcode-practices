class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search to find how many elemnets to select from the smaller array
        # since everything is sorted, we only need to check if max(l1, l2) < min(r1, r2):
        # the biggest left elements picked from num1 and num2 are smaller than the smallest element on the right hand side

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        left_side = (n1 + n2 + 1) // 2
        l, r = 0, n1 - 1
        while l <= r:
            m1 = (l + r) // 2
            m2 = left_side - m1
            l1 = nums1[m1 - 1] if m1 > 0 else float(-inf)
            l2 = nums2[m2 - 1] if m2 > 0 else float(-inf)
            r1 = nums1[m1] if n1 > m1 else float(inf)
            r2 = nums2[m2] if n2 > m2 else float(inf)
            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                r = m1 - 1
            else:
                l = m1 + 1
        
        return 0.0


                
