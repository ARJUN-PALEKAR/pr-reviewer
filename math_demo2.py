    # A perfectly fine, simple multiplication function
return a * b

def factorial(n):
    # Classic recursive factorial function
    # Wait, what happens if someone types factorial
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

# Let's test them out
print("Multiplying 6 and 8:", multiply(6, 8))
print("Factorial of 5 is:", factorial(5))