# Sure, let's simplify the explanation for kids:

# Imagine you have a number, like 7. To find its factorial, you multiply that number by all the positive whole numbers smaller than it. 
# So, for 7, it's 7 × 6 × 5 × 4 × 3 × 2 × 1. We write this as 7! (pronounced "7 factorial").

# For example:
# \[7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040\]

# Even if you have the number 0, its factorial is defined to be 1. So, \(0! = 1\).

# In simple terms, the factorial of a number is just multiplying that number by all the smaller whole numbers down to 1.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
