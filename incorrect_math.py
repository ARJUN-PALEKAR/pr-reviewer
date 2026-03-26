def divide_numbers(a, b):
    # FLAW 1: If someone passes 0 for b, the whole app crashes!
    return a / b

def calculate_factorial(n):
    # FLAW 2: If someone passes a negative number, this runs forever.
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

print("10 divided by 2 is:", divide_numbers(10, 2))
print("Factorial of 5 is:", calculate_factorial(5))