def add_numbers(a, b):
    # A perfectly fine, simple addition function
    return a + b

def fibonacci(n):
    # This is a classic recursive function.
    # It works, but it is incredibly slow for large numbers!
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Let's test them out
print("Adding 5 and 7:", add_numbers(5, 7))
print("The 10th Fibonacci number is:", fibonacci(10))