class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search to find how many elemnets to select from the smaller array
        # since everything is sorted, we only need to check if max(l1, l2) < min(r1, r2):
        # the biggest left elements picked from num1 and num2 are smaller than the smallest element on the right hand side

        n1, n2 = len(nums1), len(n2)
        n_side = (n1 + n2 + 1) // 2
        median = [0]
        if n1 == n2:
            helper(nums1, nums2, 0, len(nums1)-1, True)
        elif n2 > n1:
            helper(nums1, nums2, 0, len(nums1)-1, False)
        else:
            helper(nums2, nums1, 0, len(nums2)-1, False)
        
        # here list1 is the list we choose m elements from, list2 we choose (n_side - m) elements
        def helper(list1, list2, l, r, even):
            if l > r:
                return 
            m1 = (l + r) // 2 # pick m elements from l1
            m2 = n_side - m1
            
            l1 = list1[m1-1] if m1 > 0 else None
            l2 = list2[m2-1] if m2 > 0 else None
            r1, r2 = list1[m1], list2[m2]
            if check(l1, l2, r1, r2):
                if even:
                    res[0] = (max(l1,l2) + min(r1, r2)) // 2
                else:
                    res[0] = max(l1, l2)
            else:
                if l1 and l2 and l1 > r2:
                    helper(list1, list2, l, m1 - 1, even)
                else:
                    helper(list1, list2, m1 + 1, r, even)

                
