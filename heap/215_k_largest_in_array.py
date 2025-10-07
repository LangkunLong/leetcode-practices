class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        # no sorting, how do we rank elements? 
        # partition the array based on a pivot, use pointer p to track how many elemnts in the array are smaller than pivot
        # if have pointer p == N - k, then we have reached the spot with k's largest elemment
        # if nums[i] smaller than p, we swap positions with p, and increment p, 
        # if not, we don't swap, don't increment p but we still traverse the array (since not sorted can have other elements smaller)
        def partition(l, r):
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]  # move pivot to end
            p, pivot = l, nums[r]
            for i in range(l, r): # don't need to look at last value since that is the pivot
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            # have to swap pivot
            nums[p], nums[r] = nums[r], nums[p]
            #print(p)

            if len(nums) - k > p: return partition(p+1, r)
            elif len(nums) - k < p: return partition(l, p-1)
            else: 
                #print(nums[p])
                return nums[p]
        return partition(0, len(nums)-1)

        # nums.sort()
        # return nums[len(nums)-k]
