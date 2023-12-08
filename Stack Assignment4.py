# 7.Write a program that converts an infix expression into an equivalent postfix expression. The rules to convert an infix expression into an equivalent postfix expression are as follows:
# Suppose infx represents the infix expression and pfx represents the postfix expression. The rules to convert infx into pfx are as follows:
# a.Initialize pfx to an empty expression and also initialize the stack.
# b.Get the next symbol, sym, from infx.
# b.1. If sym is an operand, append sym to pfx.
# b.2. If sym is (, push sym into the stack.
# b.3. If sym is ), pop and append all the symbols from the stack until the most recent left parenthesis. Pop and discard the left parenthesis.
# b.4. If sym is an operator:
# b.4.1. Pop and append all the operators from the stack to pfx that are above the  most recent left parenthesis and have precedence greater than or equal to sym.
# b.4.2. Push sym onto the stack.
# c.After processing infx, some operators might be left in the stack. Pop and append to pfx everything from the stack.

# In this program, you will consider the following (binary) arithmetic operators: +, -, *, /. You may assume that the expressions you will process are error free.

# Design a class that stores the infix and postfix strings. The class must include the following operations:
# •getInfix—Stores the infix expression
# •showInfix—Outputs the infix expression
# •showPostfix—Outputs the postfix expression
# Some other operations that you might need are the following:
# •convertToPostfix—Converts the infix expression into a postfix expression. The resulting postfix expression is stored in pfx.
# •precedence—Determines the precedence between two operators. If the first operator is of higher or equal precedence than the second operator, it returns the value true; otherwise, it returns the value false.

# Include the constructors and destructors for automatic initialization and dynamic memory deallocation.

# Test your program on the following five expressions:
# A + B - C;
# (A + B ) * C;
# (A + B) * (C - D);
# A + ((B + C) * (E - F) - G) / (H - I);
# A + B * (C + D ) - E / F * G + H;

For each expression, your answer must be in the following form:
Infix Expression: A + B - C;
Postfix Expression: A B + C -
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
