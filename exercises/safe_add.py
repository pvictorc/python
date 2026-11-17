# Step 1: Reuse the add function
def add(a, b):
    return a + b

# Step 2: Write the safe_add function with a try-except block
def safe_add(a, b):
    try:
        return add(a, b)
    except TypeError as e:
        return f"Error: Invalid input types for addition - {e}"
    
def safe_add2(a,b):
    try:
        return add(a,b);
    except TypeError as e:
        return f"Erro: Tipo de Input inválido para adição - {e}"

# Step 3: Create a list of inputs as tuples
inputs = [
    (5, "Python"),   # Invalid: int + str
    (3, 5.2),        # Valid: int + float
    (2, 5)           # Valid: int + int
]

# Step 4: Use a for loop to iterate through the inputs and call safe_add
for a, b in inputs:
    result = safe_add2(a, b)
    print(f"safe_add({a}, {b}) = {result}")

# Expected output:
# safe_add(5, Python) = Error: Invalid input types for addition - unsupported operand type(s) for +: 'int' and 'str'
# safe_add(3, 5.2) = 8.2
# safe_add(2, 5) = 7