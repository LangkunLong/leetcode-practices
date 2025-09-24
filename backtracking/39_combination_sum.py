class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # optimized approach is to define decision tree so that we single out each digit 
        # 2 decision, either solution contain an occurrence of this digit, or do not contain 
        # an occurrence of a digit

        res = []
        
        def backtrack(sub_comb, cur_index, path):
            # base case
            if path == target:
                res.append(sub_comb)
                return 
            if path > target:
                return 
            for start in range(cur_index, len(candidates)):
                
                # all possible solutions containing (adding) 1 occurrence of candidate[i]
                # only need 1 recursion because the for loop will traverse all possible index
                # next iteration of see all possible solutions containing (adding 1 occurrence)
                # of candidate[i + 1]
                backtrack(sub_comb + [candidates[start]], start, path + candidates[start])
        
        backtrack([], 0, 0)
        return res
