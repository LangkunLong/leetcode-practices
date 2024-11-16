class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # each line has exactly maxWidth characters; left and right justified 
        # pack as many words as you can, pad extra spaces so each line has exactly maxWidth characters
        # need to determine left and right ending words
        # by default needs 1 space, need to check maxmium words we can fit, determine starting and ending words in the line 
        justified_text = []
        i = 0
        while i < len(words):
            word_length = len(words[i])
            last_word = i+1 
            # traverse to determine last word in line
            while last_word < len(words) and word_length + len(words[last_word]) + last_word - i <= maxWidth:
                word_length += len(words[last_word])
                last_word += 1

            num_words = last_word - i 
            line = ""
            # left justified if last word in line is last word in sentence or if only 1 word in line
            if num_words == 1 or last_word == len(words):
                line = " ".join(words[i:last_word])
                remaining_space = maxWidth - len(line)
                line += " " * remaining_space
            else:
                # fully justified spacing:
                gaps = num_words - 1
                space_size, remaining_space = divmod(maxWidth - word_length, gaps)
                # for the first (remaining_space) words, each word get an extra space, until no extra space left
                for j in range(remaining_space):
                    line += words[i + j] + " " * (space_size + 1)
                # rest of the words get regular space until the last word
                for j in range(remaining_space, num_words-1):
                    #print(words[i+j])
                    line += words[i + j] + " " * space_size
                # last word has no space
                line += words[last_word - 1]
            
            justified_text.append(line)
            i = last_word
        
        return justified_text