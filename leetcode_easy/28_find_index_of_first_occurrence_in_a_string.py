class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0

        if needle in haystack:
            # for char in range(len(haystack)):
            #     if haystack[char] == needle[0]:
            #         match = True
            #         for needle_char in range(len(needle)):
            #             print(needle[needle_char], haystack[char + needle_char])
            #             if needle[needle_char] != haystack[char + needle_char]:
            #                 match = False
            #                 break
            #         if match:
            #             return char
            # return -1

            # faster to use a sliding window and compare substrings instead of characters:
            n, h = len(needle), len(haystack)
            for i in range(h - n + 1):
                if haystack[i:i+n] == needle:
                    return i
            return -1
        else:
            return -1