class Solution:
    def isValid(self, s: str) -> bool:
        op = "{(["
        list = []
        for c in s:
            if c in op:
                list.append(c)
            else:  # found closing parenthesis
                if len(list) == 0:
                    return False
                else:
                    if c == '}' and list[-1] == '{':
                        list.pop(-1)
                    elif c == ')' and list[-1] == '(':
                        list.pop(-1)
                    elif c == ']' and list[-1] == '[':
                        list.pop(-1)
                    else:
                        return False
        if len(list) == 0:
            return True
        else:
            return False


s = Solution()
print(s.isValid("{([])}"))
