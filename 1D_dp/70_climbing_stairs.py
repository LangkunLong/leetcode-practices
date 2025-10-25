# nice easy problem to introduce DP
# at first was doing backtracking to generate all possible ways to reach n, but TLE
# don't need to generate all combinations, at each step, keep all the ways to go to step -2, and all the ways to go to step -1, and add them together
# use memorization to store ways to climb at each step; 8 -> 6, 7; 6 -> 4, 5; 7 -> 5,6; 4 -> 2 (return), 3; 3->1(return), 2(return), store 3
# 4 -> 2 (return), 3(return, since we stored it), so 4 returns; 5-> 3(return), 4(return); 6-> 4(return), 5(return) ....
class Solution:
    def climbStairs(self, n: int) -> int:

        # explicit approach to help me understand
        mem_dict = dict()
        mem_dict[1] = 1
        mem_dict[2] = 2
        def helper(n):
            if n == 1 or n == 2:
                return mem_dict[n]
            elif n > 2:
                if n-2 not in mem_dict or n-1 not in mem_dict:
                    mem_dict[n-2] = helper(n-2)
                    mem_dict[n-1] = helper(n-1)
                mem_dict[n] = mem_dict[n-2] + mem_dict[n-1]
                return mem_dict[n]

        helper(n)
        return mem_dict[n]

        # optimized solution: 
        # bottom up approach with O(1) memory instead of O(N), we don't need to keep track of entire array
        # only need previous 2 elements
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp

        return one

            

            
