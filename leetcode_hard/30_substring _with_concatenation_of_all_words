class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        left = 0
        total_length = len(words) * len(words[0])
        word_length = len(words[0])

        if total_length > len(s): #not possible to have permutation is substring is longer than string
            return []
        
        if s == "" or words == []:
            return []

        from collections import Counter
        # use frequency map to count up occurrences:
        expected_freq = Counter(words)
        solutions = []
        # cannot gurantee that (s) is all words concacanated together, need to use sliding window to check each one
        while left + total_length <= len(s):
            sub_string = s[left:left + total_length]
            # split sub_string into words 
            sub_string_words = []
            for i in range(0, total_length, word_length):
                sub_string_words.append(sub_string[i:i+word_length])
            
            actual_freq = Counter(sub_string_words)
            
            if actual_freq == expected_freq:
                solutions.append(left)
            left += 1
       
        return solutions
