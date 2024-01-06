# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
lambda_add = lambda x, y: x + y

# Using the functions
result1 = add(3, 5)
result2 = lambda_add(3, 5)

print("Result from regular function:", result1)
print("Result from lambda function:", result2)
