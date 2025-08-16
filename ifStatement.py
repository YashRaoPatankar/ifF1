# working with multiple if statements
op1 = int(input("Enter first number: "))
op2 = int(input("Enter second number: "))
op = input("Enter the operation (+, -, *, /): ")
if op == "+":
    result = op1 + op2
elif op == "-":
    result = op1 - op2
elif op == "*":
    result = op1 * op2
elif op == "/":
    if op2 != 0:
        result = op1 / op2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"        
print(f"The result of {op1} {op} {op2} is: {result}")