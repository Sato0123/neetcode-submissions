class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+" | "-" | "*" | "/":
                    b = int(stack.pop())
                    a = int(stack.pop())
                    match token:
                        case "+":
                            stack.append(a + b)
                        case "-":
                            stack.append(a - b)
                        case "*":
                            stack.append(a * b)
                        case "/":
                            stack.append(a / b)
                case _:
                    stack.append(token)

        return int(stack[0])

