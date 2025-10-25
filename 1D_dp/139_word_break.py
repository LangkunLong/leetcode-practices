class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # use start and end to mark subwindwow, if subwindow ever forms a word, update status to true
        # after identifying to true, move subwindow to next available window
        l, r = 0, 0
        status = False
        for char in s:
            if s[l:r] in wordDict:
                l += 1
                r += 1
                status = True
            else:
                r += 1
