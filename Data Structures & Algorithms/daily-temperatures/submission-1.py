class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            today = temperatures[i]
            while stack and today > temperatures[stack[-1]]:
                top = stack.pop()
                result[top] = i - top
            stack.append(i)

        return result
