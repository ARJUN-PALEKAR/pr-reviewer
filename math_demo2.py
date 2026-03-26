def calculate_factorial(n):
    # FLAW 1: If someone passes a negative number, this will run forever and crash!
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

def divide_numbers(a, b):
    # FLAW 2: No safety check. If b is 0, the whole app crashes.
    return a / b

def slow_fibonacci(n):
    # FLAW 3: Terrible time complexity. This will freeze if n is a big number.
    if n <= 1:
        return n
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)

if _name_ == "_main_":
    print("Factorial of 5:", calculate_factorial(5))
    print("10 divided by 2 is:", divide_numbers(10, 2))
    print("Fibonacci of 10 is:", slow_fibonacci(10))