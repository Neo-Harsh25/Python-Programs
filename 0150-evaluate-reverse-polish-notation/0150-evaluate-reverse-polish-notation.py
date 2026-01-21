class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # division
                    result = abs(a) // abs(b) # abs -- absolut  built in function
                    if (a < 0) ^ (b < 0):  # if signs differ
                        result = -result
                    stack.append(result)
        
        return stack.pop()