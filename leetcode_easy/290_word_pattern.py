class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # same question as if string is isotophoic except here string is a string of words
        pattern_dict = dict()
        string_dict = dict()
        str_len = len(pattern)
        s_list = s.split()

        if len(s_list) != str_len:
            return False
        
        for i in range(str_len):
            pattern_dict[pattern[i]] = s_list[i]
            string_dict[s_list[i]] = pattern[i]
        
        for i in range(str_len):
            if pattern_dict[pattern[i]] != s_list[i] or string_dict[s_list[i]] != pattern[i]:
                return False

        return True