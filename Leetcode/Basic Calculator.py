class Solution(object):
    def calculate(self, s):
        result, sign, current, stack = 0, 1, 0, []
        for element in s:
            if element.isdigit():
                current = current * 10 + int(element)
            elif element in "+-":
                result += current * sign
                current = 0
                sign = 1 if element == "+" else -1
            elif element == "(":
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1
            elif element == ")":
                result += current * sign
                result *= stack.pop()
                result += stack.pop()
                current, sign = 0, 1
        return result + (sign * current)
        