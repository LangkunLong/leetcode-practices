class Solution:
    def isHappy(self, n: int) -> bool:
        # add up the square of all its digits, but how do i know if its looping 
        if n == 1:
            return True
        
        # detect cycle using a set, if a number repeats, then its a cycle
        cycle = set()
        while n != 1 :
            n = sum(int(num)**2 for num in str(n))
            if n in cycle:
                return False
            cycle.add(n)

        return True