def minWindow(self, s: str, t: str) -> str:
        # use frequency counter to track char occurrences
        # move window to the right, then while maintaining the same occurrences, minimize window size 
        # use a dictionary to store occurrences
        # edge case:
        if not s or not t:
            return ""
        
        left = 0
        exp_freq = Counter(t)
        exp_num_chars = len(exp_freq)
        act_freq = {}
        act_num_chars = 0
        min_window_length = float(inf)
        min_window = ""
        for right in range(len(s)):
            right_char = s[right]
            act_freq[right_char] = act_freq.get(right_char, 0) + 1

            # check if char in t is present in current window and need frequency to match
            if right_char in t and exp_freq[right_char] == act_freq[right_char]:
                act_num_chars += 1

            # can decrement window when current window has all the characters of t
            while act_num_chars == exp_num_chars and left <= right:
                if len(s[left:right+1]) < min_window_length:
                    min_window = s[left:right + 1]
                    min_window_length = len(s[left:right+1])
                
                # slide left window to the right
                left_char = s[left]
                act_freq[left_char] -= 1
                if left_char in t and exp_freq[left_char] > act_freq[left_char]:
                    act_num_chars -= 1
                left += 1

            right += 1
        
        return min_window if min_window_length != float(inf) else ""