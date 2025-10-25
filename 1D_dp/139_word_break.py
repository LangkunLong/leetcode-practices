class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # decision tree is based on available words in wordDict\
        # base case is when reading position len(s), means we have matched all words including the last element
        # starting from the base case len(s), work backwards
