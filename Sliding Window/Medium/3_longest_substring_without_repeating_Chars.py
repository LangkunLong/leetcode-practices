class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        duplicate = set()
        left = 0
        longest = 1
        for right in range(len(s)):
            if s[right] not in duplicate:
                longest = max(longest, right - left + 1)
                duplicate.add(s[right])
            else:
                while s[right] in duplicate:
                    duplicate.remove(s[left])
                    left += 1
                duplicate.add(s[right])

        return longest

