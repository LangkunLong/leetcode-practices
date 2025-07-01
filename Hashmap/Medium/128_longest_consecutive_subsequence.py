class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # cannot sort, since takes at least O(nlogn)
        # store the neighbor entries ex: [100] = [99, 101]
        # append possible neighbors in a list: store 100, 99, 101; this approach doesn't work because cannot account for redundant entries 
        # convert nums to a set so only unique entries, can check if the next element exists, make sure that no num-1 exists, if exists, set that at the start element
        # each element is processed at most twice, once to check if its the starting point, and once to see if it is consecutive, O(2n)
        num_set = set(nums)
        longest = 0
        for num in num_set:
            sub_sequence = 0
            if num-1 not in num_set:
                start = num
                sub_sequence += 1
                while start+1 in num_set:
                    sub_sequence += 1
                    start += 1
            longest = max(longest, sub_sequence)
        return longest

    


            


