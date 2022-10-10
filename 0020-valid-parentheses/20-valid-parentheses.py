class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = []
        for bracket in s:
            if (bracket == '(') or (bracket == '{') or (bracket == '['):
                parenStack.append(bracket)
            else:
                if len(parenStack) == 0:
                    return False
                    
                openBracket = parenStack.pop()
                if bracket == ')' and openBracket != '(':
                    return False
                if bracket == '}' and openBracket != '{':
                    return False
                if bracket == ']' and openBracket != '[':
                    return False
        
        if len(parenStack) > 0:
            return False

        return True
