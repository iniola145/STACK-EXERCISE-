#5.Write a function to convert a number from base 2 to base 10. To convert a number from base 2 to base 10, we first find the weight of each bit in the binary number. The weight of each bit in the binary number is assigned from right to left. The weight of the rightmost bit is 0. The weight of the bit immediately to the left of the rightmost bit is 1, the weight of the bit immediately to the left of it is 2, and so on. Consider the binary number 1001101. The weight of each bit is as follows:
# weight 		6 5 4 3 2 1 0
# 10 0 1 1 0 1
# We use the weight of each bit to find the equivalent decimal number. For each bit, we multiply the bit by 2 to the power of its weight, and then we add all of the numbers. For the binary number 1001101, the equivalent decimal number is

# To write a program that converts a binary number into the equivalent decimal number, we note two things: 
# -The weight of each bit in the binary number must be known, and 
# -the weight is assigned from right to left. 
# Because we do not know in advance how many bits are in the binary number, we must process the bits from right to left. After processing a bit, we can add 1 to its weight, giving the weight of the bit immediately to its left. Also, each bit must be extracted from the binary number and multiplied by 2 to the power of its weight. To extract a bit, you can use the mod operator. Write a program that uses a stack to convert a binary number into an equivalent decimal number and test your function for the following values: 11000101, 10101010, 11111111, 10000000, 1111100000.
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
