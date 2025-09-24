class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # our decision tree is all the numbers not including itself
        # can only use digits not in our current permutation

        if not nums:
            return []
        
        res = []
        #cur_perm = [], cur_digit = 
        def backtrack(cur_perm):
            # base case
            if len(cur_perm) == len(nums):
                res.append(cur_perm)
                return 
            # [1,2,3]
            for digit in nums:
                # is 1 in []? no, backtrack[1]
                # is 1 in [1], yes, return
                # is 2 in [1], no, backtrack[1,2]
                # is 1 in [1,2], yes, return
                # is 2 in [1,2], yes, return 
                # is 3 in [1,2,3], no, backtrack[1,2,3]
                # base case, append + return 
                # is 3 in [1], no, backtrack[1,3]
                if digit not in cur_perm:
                    backtrack(cur_perm + [digit])
        backtrack([])
        return res
