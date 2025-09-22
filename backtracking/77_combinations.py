class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #define base case
        res = []

        def backtrack(start, sub_res):
            
            if len(sub_res) == k:
                res.append(sub_res.copy())
                return 
            for i in range(start, n + 1):
                sub_res.append(i)
                backtrack(i+1, sub_res)
                sub_res.pop()
        
        backtrack(1, [])
        return res
                
