#4.Write a program that uses a stack to print the prime factors of a positive integer in descending order.
def get_prime_factors(num):
    factors = []
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1

    return factors

def prime_factors_stack(n):
    prime_factors = get_prime_factors(n)
    factors_stack = []

    for factor in reversed(prime_factors):
        factors_stack.append(factor)

    return factors_stack

# Input: Positive Integer
num = int(input("Enter a positive integer: "))

# Get prime factors in descending order using a stack
factors_stack = prime_factors_stack(num)

# Print prime factors in descending order
print(f"Prime factors of {num} in descending order: {[factor for factor in reversed(factors_stack)]}")
