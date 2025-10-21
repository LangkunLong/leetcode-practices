# why can't solve with 2 pointers??
# can't assume array are same lengths
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 2 pointer approach
        l1, l2 = 0, 0
        res = []
        for i in range(k):
            if l1 < len(nums1) and l2 < len(nums2):
                res.append([nums1[l1], nums2[l2]])
                if nums1[l1] < nums2[l2]:
                    l2 += 1
                else:
                    l1 += 1
            else:
                if l1 == len(nums1):
                    l2 += 1
                    l1 = 0
                else:
                    l1 += 1
                    l2 = 0

        return res

