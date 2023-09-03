def branch10(a, b, operation):
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b != 0:
            result = a / b
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation"
    
    if result < 0:
        return "Result is negative"
    elif result == 0:
        return "Result is zero"
    elif result > 0 and result < 10:
        return "Result is positive and less than 10"
    else:
        return "Result is positive and greater than or equal to 10"