class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                lst.append(i)
            else:
                if lst:
                    if lst[-1] == '(' and i == ')':
                        lst.pop()
                    elif lst[-1] == '{' and i == '}':
                        lst.pop()
                    elif lst[-1] == '[' and i == ']':
                        lst.pop()
                    else:
                        return False
                else:
                    return False
        if lst:
            return False
        return True
