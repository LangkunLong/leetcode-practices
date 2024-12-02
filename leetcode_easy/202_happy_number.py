class Solution:
    def isHappy(self, n: int) -> bool:
        # add up the square of all its digits, but how do i know if its looping 
        if n == 1:
            return True


        while n != 1 and len(str(n)) != 1:
            str_int = str(n)
            temp_num = 0
            for char in str_int:
                temp_num += (int(char) ** 2)
            if temp_num == 1:
                return True
            print(temp_num)
            n = temp_num
        return False