class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None:
            return ""

        sorted_str = sorted(strs, key=lambda x: len(x))
        smallest_word = sorted_str[0]
        #print(smallest_word)
        prefix = ""
        word_prefix = ""
        for char in range(len(smallest_word)):
            word_prefix += smallest_word[char] # append with a new char each time
            #print(word_prefix)
            for word in range(1, len(sorted_str)):
                #print(sorted_str[word][0:len(word_prefix)])
                if word_prefix != sorted_str[word][0:len(word_prefix)]:
                    return prefix
            prefix = word_prefix
            #print(prefix)
        return prefix

