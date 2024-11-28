class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # anagram is word that contains the same characters
        # if strs == None or strs == []:
        #     return []
        # if strs == [""]:
        #     return [[""]]
        
        # #brute force solution O(n^2)
        # from collections import Counter
        # result = []
        # marker = [False for _ in range(len(strs))]
        # #marker = [False for _ in range(len(strs))]
        # for i in range(len(strs)):
        #     temp_result = []
        #     if marker[i] ==  False:
        #         temp_result.append(strs[i])
        #         marker[i] = True
        #     #print("outer word: ", strs[i])
        #     for j in range(i+1, len(strs)):
        #         #print(strs[j])
        #         if Counter(strs[i]) == Counter(strs[j]) and i != j and marker[j] == False:
        #             temp_result.append(strs[j])
        #             marker[j] = True
        #     if temp_result != []:
        #         result.append(temp_result)
        # #print(marker)
        # return result

        # better solution: sort each string and use that string as key in the dictionary, whenever
        # another string is an angram, the sorted string form will be the same, so can append to the same key
        # or can use a character count as key, as long as different words map to the same key 
        word_dict = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in word_dict:
                word_dict[sorted_word] = list()
            word_dict[sorted_word].append(word)

        return list(word_dict.values())

