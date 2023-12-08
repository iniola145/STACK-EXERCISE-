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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def binary_to_decimal(binary_number):
    stack = Stack()
    decimal_number = 0
    weight = 0

    for bit in binary_number:
        stack.push(int(bit))

    while not stack.is_empty():
        decimal_number += stack.pop() * (2 ** weight)
        weight += 1

    return decimal_number

# Test the function
binary_numbers = ["11000101", "10101010", "11111111", "10000000", "1111100000"]

for binary_number in binary_numbers:
    decimal_result = binary_to_decimal(binary_number)
    print(f"Binary: {binary_number} -> Decimal: {decimal_result}")
