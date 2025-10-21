# why can't solve with 2 pointers??
# can't assume array are same lengths
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 2 pointer approach
        l1, l2 = 0, 0
        res = []
        for i in range(k):
            if nums1[l1] < nums2[l2]:
                res.append([nums1[l1], nums2[l2]])
                l2 += 1
            else:
                res.append([nums1[l1], nums2[l2]])
                l1 += 1
        return res
