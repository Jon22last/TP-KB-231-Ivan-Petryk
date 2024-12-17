class ReversePolishNotation:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def to_rpn(self, expression):
        output = []
        stack = []

        for token in expression.split():
            if token.isnumeric():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':  
                    output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
            else:
                while (stack and stack[-1] != '(' and
                       self.operators.get(stack[-1], 0) >= self.operators.get(token, 0)):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output

    def evaluate_rpn(self, rpn_expression):

        stack = []

        for token in rpn_expression:
            if token.isnumeric():
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)

        return stack[0]

if __name__ == "__main__":
    expression = input("Enter an expression: ")
    rpn_converter = ReversePolishNotation()

    rpn = rpn_converter.to_rpn(expression)
    print("Reverse Polish Notation:", " ".join(rpn))

    result = rpn_converter.evaluate_rpn(rpn)
    print("Result:", result)
