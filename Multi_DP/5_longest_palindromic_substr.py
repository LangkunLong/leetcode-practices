class Solution:
    def longestPalindrome(self, s: str) -> str:
        # at each index, base case is starting a substring with that index
        # at index 2: {start substring with b: 1
        #              attach to 'a', 'ab' : 0
        #              attach to 'ba', 'bab': 3}
        longest = ""
        length = 0
        for i in range(len(s)):
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > length:
                    longest = s[l:r+1]
                    length = r-l + 1
                l -= 1
                r += 1
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > length:
                    longest = s[l:r+1]
                    length = r-l + 1
                l -= 1
                r += 1
        return longest
                
