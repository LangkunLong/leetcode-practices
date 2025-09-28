class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # decision tree is to append either an '(' or ')'
        # base case: if len(sub_str) is 2n, check if valid, then we append solution

        res = []
        def backtrack(cur_par):
            if len(cur_par) == 2*n and valid(cur_par):
                res.append("".join(cur_par))
                return 
            
            for path in ['(', ')']:
                cur_par.append(path)
                if valid(cur_par):
                    backtrack(cur_par)
                cur_par.pop()
        
        
        def valid(sub_sol):
            if len(sub_sol) < 2*n:
                n_open, n_close = 0,0
                for par in sub_sol:
                    if par == '(':
                        n_open += 1
                    else:
                        n_close += 1
                if n_open > n or n_close > n:
                    return False
            else:
                stack = [] 
                for par in sub_sol:
                    if par == '(':
                        stack.append(par)
                    else:
                        if stack:
                            close = stack.pop()
                            if close != '(':
                                return False
                        else:
                            return False
                if len(stack) != 0:
                    return False
            return True
        backtrack([])

        return res
