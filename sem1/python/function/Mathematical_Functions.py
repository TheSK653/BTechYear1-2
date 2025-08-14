def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."
# Test the functions
result_add = add(5, 3)
result_subtract = subtract(8, 4)
result_multiply = multiply(2, 6)
result_divide = divide(10, 2)
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")