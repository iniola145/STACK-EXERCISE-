#6.Write a program that uses a stack to convert a decimal number into an equivalent binary number.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

def decimal_to_binary(decimal_number):
    stack = Stack()

    while decimal_number > 0:
        remainder = decimal_number % 2
        stack.push(remainder)
        decimal_number //= 2

    binary_number = ""
    while not stack.is_empty():
        binary_number += str(stack.pop())

    return binary_number if binary_number else "0"

# Test the function
decimal_numbers = [10, 45, 128, 255, 1000]

for decimal_number in decimal_numbers:
    binary_result = decimal_to_binary(decimal_number)
    print(f"Decimal: {decimal_number} -> Binary: {binary_result}")
