# nice easy problem to introduce DP
# at first was doing backtracking to generate all possible ways to reach n, but TLE
# don't need to generate all combinations, at each step, keep all the ways to go to step -2, and all the ways to go to step -1, and add them together
# use memorization to store ways to climb at each step; 8 -> 6, 7; 6 -> 4, 5; 7 -> 5,6; 4 -> 2 (return), 3; 3->1(return), 2(return), store 3
# 4 -> 2 (return), 3(return, since we stored it), so 4 returns; 5-> 3(return), 4(return); 6-> 4(return), 5(return) ....
