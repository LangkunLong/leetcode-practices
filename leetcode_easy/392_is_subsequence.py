class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # thinking of using 2 pointers:
        subseq_ptr = 0
        t_ptr = 0
        while subseq_ptr < len(s) and t_ptr < len(t):
            if s[subseq_ptr] == t[t_ptr]:
                subseq_ptr += 1
            t_ptr += 1
            
        if subseq_ptr == len(s):
            return True
        else:
            return False