class Solution:
    def longestPalindrome(self, s: str) -> str:
        # starting in the middle, and expand to left and right
        # assume each element is center of palindrome, expand left and right
        # O(n^2) solution, for each element, check the longest valid palindrome it can form
        
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
                
