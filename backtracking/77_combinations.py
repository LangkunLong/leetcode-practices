class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #define base case
        res = []
        sub_res = []

        def backtrack(j):
            
            if len(sub_res) == k:
                res.append(sub_res)
                return 
            for i in range(j, n + 1):
                backtrack(i+1, sub_res.append(i))
                sub_res = [] # clear after return 
        
        backtrack(1)
        return res
                
