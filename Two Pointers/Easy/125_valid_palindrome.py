class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        if len(s) == 1:
            return True
        s_stripped = s.lower()
        # regex expression to substitue non-alphaneumeirc characters into empty string
        s_stripped = re.sub(r'[^a-zA-Z0-9]', '', s_stripped)
        first_ptr, last_ptr = 0, len(s_stripped) - 1
        while first_ptr < last_ptr:
            if s_stripped[first_ptr] != s_stripped[last_ptr]:
                return False
            first_ptr += 1
            last_ptr -= 1
        
        return True