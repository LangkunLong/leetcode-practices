class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # decision tree is based on available words in wordDict\
        # base case is when reading position len(s), means we have matched all words including the last element
        # starting from the base case len(s), work backwards
        dp = [False for char in range(len(s) + 1)]
        dp[len(s)] = True
        # start inclusive, end non-inclusive, start at last element, end at -1 to include 0
        for i in range(len(s)-1, -1, -1):
            #print(s[i:])
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    #print(s[i : i + len(word)])
                    dp[i] = dp[i + len(word)] # at base case dp[len(s)] is true
                    #print(dp)
                # if true, want to maintain true, want to break out of checking all other words because other words
                # might have a different breaking combination, only keep looking if false and have not gone through 
                # all the words yet
                if dp[i]:
                    break

        return dp[0]
