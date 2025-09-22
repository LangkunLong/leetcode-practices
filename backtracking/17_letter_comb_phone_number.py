class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # use a mapping dictionary for each number to dict
        # backtrack to all possible branches, go to next digit + next cur
        # ALWAYS DEFINE BASE CASE FIRST
        map_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def backtrack(cur_pos, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return 
            # cur_pos starts at 0
            for c in map_dict[digits[cur_pos]]:
                backtrack(cur_pos + 1, cur_str + c)
        if digits:
            backtrack(0, "")
        
        return res
        
                        


                
