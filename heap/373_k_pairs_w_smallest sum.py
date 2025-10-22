class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # need to compare sums, since given non-decreasing, we can explore next index elements
        import heapq
        min_sum = []
        res = []
        heapq.heappush(min_sum, (nums1[0]+nums2[0], 0, 0))
        #visited = set()

        for i in range(k):
            p_sum, n1, n2 = heapq.heappop(min_sum)
            #visited.add((n1,n2))
            res.append([nums1[n1], nums2[n2]])
            if n1 + 1 < len(nums1): #and (n1 + 1, n2) not in visited:
                heapq.heappush( min_sum, ( nums1[n1+1]+nums2[n2], n1 + 1, n2))
                #visited.add((n1+1, n2))
            if n2 +1 < len(nums2): #and (n1, n2+1) not in visited:
                heapq.heappush( min_sum, ( nums1[n1]+nums2[n2+1], n1, n2+1))
                #visited.add((n1, n2+1))
        return res
