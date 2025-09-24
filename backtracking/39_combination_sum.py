class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import Counter
        res = []
        def backtrack(sub_comb):
            if sum(sub_comb) == target:
                cur_count = Counter(sub_comb)
                for exi_res in res:
                    # solution exists
                    if Counter(exi_res) == cur_count:
                        return 
                res.append(sub_comb)
            if sum(sub_comb) > target:
                return 
            
            for digit in candidates:
                backtrack(sub_comb + [digit])
        
        backtrack([])
        return res
