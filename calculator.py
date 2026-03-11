# Prompt for inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operator (+, -, *, /): ")

# Calculate based on operator
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Basic division check to prevent crashes
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operator"

# Display the result
print(f"The result is: {result}")
