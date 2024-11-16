class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # cannot just count new substring after enconutering duplicates, because in bewteen substring can be the new start, maintain a left pointer and whenever encounter duplicate, increment left pointer to the next index, need to maintain right most position of left pointer 
        length = 0
        left = 0
        chars = set()
        cur_length = 0
        for right, char in enumerate(s):
            while char in chars:
                chars.remove(s[left])
                left += 1
            chars.add(char)
            length = max(length, right-left + 1)
        
        return length