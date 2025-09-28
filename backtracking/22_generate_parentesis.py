class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # decision tree is to append either an '(' or ')'
        # optimized approach, can only add ')' if we have more open brackets
        # open brackets and close brackets capped by n
        # don't need to use a stack to verfiy because if we follow these rules the parenthesis
        # will be valid

        res = []
        def backtrack(cur_par, n_open, n_close):
            if n_open == n and n_close == n:
                res.append("".join(cur_par))
                return 
            if n_open < n :
                cur_par.append('(')
                backtrack(cur_par, n_open + 1, n_close)
                cur_par.pop()

            if n_close < n_open:
                cur_par.append(')')
                backtrack(cur_par, n_open, n_close + 1)
                cur_par.pop()

        backtrack([], 0, 0)
        return res
