class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # use python counter
        from collections import Counter
        char_used = Counter(magazine)
        
        for char in ransomNote:
            if char_used.get(char, 0) == 0:
                return False
            char_used[char] -= 1
        
        return True