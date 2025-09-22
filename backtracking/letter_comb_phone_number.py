class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # use a mapping dictionary for each number to dict
        # brute force can separate starting digit with the rest of the digits
        map_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []
        
        # separate first digit 
        first, remain = digits[0], digits[1:]
        res = []
        for char in map_dict[first]:
            sub_str = char
            if remain:
                for digit in remain:
                    for c in map_dict[digit]:
                        res.append(sub_str + c)
            else:
                res.append(sub_str)
        return res
                        


                
