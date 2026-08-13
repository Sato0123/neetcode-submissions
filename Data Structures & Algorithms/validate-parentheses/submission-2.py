class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case ")":
                    if not stack or "(" != stack.pop():
                        return False
                case "}":
                    if not stack or "{" != stack.pop():
                        return False
                case "]":
                    if not stack or "[" != stack.pop():
                        return False
                case _:
                    stack.append(c)
        if stack:
            return False
        return True
