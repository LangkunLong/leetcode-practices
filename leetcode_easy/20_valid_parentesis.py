class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) % 2 != 0:
            return False
        
        # distinguish brackets by their type: open or closed
        # using last in first out (brackets must be closed in correct order
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                # no opening brackets
                if not stack:
                    return False
                if stack and char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if stack and char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if stack and char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False

        if not stack:
            return True
        else:
            return False
