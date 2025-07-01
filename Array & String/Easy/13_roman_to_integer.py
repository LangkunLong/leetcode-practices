class Solution:
    def romanToInt(self, s: str) -> int:
        # str characters in descending order
        roman_int_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        num = 0
        str_list = list(s)
        char = 0
        while char < len(str_list):
            two_chars = ''.join(str_list[char:char+2])
            if two_chars in roman_int_dict:
                num += roman_int_dict[two_chars]
                char += 2
            else:
                char_one = str_list[char]
                num += roman_int_dict[char_one]
                char += 1

        return num