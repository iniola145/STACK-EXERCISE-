class ExpressionConverter:
    def __init__(self):
        self.infix = ""
        self.postfix = ""

    def get_infix(self, expression):
        self.infix = expression

    def show_infix(self):
        print("Infix Expression:", self.infix)

    def show_postfix(self):
        print("Postfix Expression:", self.postfix)

    def convert_to_postfix(self):
        stack = []
        self.postfix = ""

        def precedence(op):
            if op == '+' or op == '-':
                return 1
            elif op == '*' or op == '/':
                return 2
            else:
                return 0

        for symbol in self.infix:
            if symbol.isalnum():
                self.postfix += symbol
            elif symbol == '(':
                stack.append(symbol)
            elif symbol == ')':
                while stack and stack[-1] != '(':
                    self.postfix += stack.pop()
                stack.pop()  # Discard '('
            elif symbol in {'+', '-', '*', '/'}:
                while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(symbol):
                    self.postfix += stack.pop()
                stack.append(symbol)

        while stack:
            self.postfix += stack.pop()

# Test the program with given expressions
expressions = [
    "A + B - C",
    "(A + B) * C",
    "(A + B) * (C - D)",
    "A + ((B + C) * (E - F) - G) / (H - I)",
    "A + B * (C + D) - E / F * G + H"
]

for expression in expressions:
    converter = ExpressionConverter()
    converter.get_infix(expression)
    converter.convert_to_postfix()
    converter.show_infix()
    converter.show_postfix()
    print()
