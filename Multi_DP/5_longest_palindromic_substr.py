class Solution:
    def longestPalindrome(self, s: str) -> str:
        # at each index, base case is starting a substring with that index
        # at index 2: {start substring with b: 1
        #              attach to 'a', 'ab' : 0
        #              attach to 'ba', 'bab': 3}
        if len(s) == 1:
            return s

        longest = ""
        for i in range(len(s)-1, -1 , -1):
            for j in range(i, len(s)):
                if self.helper(s[i:j+1]):
                    if len(s[i:j+1]) > len(longest):
                        longest = s[i:j+1]
        return longest
    
    def helper(self, s):
        l, r = 0, len(s) -1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
