"""check math expression
Task:
Create a function that takes a string input and checks if it is a mathematical expression.
Supported operators: +, -, *, /, % and only integers

Input/Output:
"5 + 2"         -->    true  
"9 * 1"         -->    true  
"hello world"   -->    false  
"123"           -->    false  
"5 + foo"       -->    false  
Addition: You can become as complex as you like on this one, working with higly complex mathematical expression."""

# Solution 1
import re

def is_math_expression(expression):
    pattern = r'^\s*\d+\s*[-+\/*%]\s*\d+\s*$'
    # ^      - Start of the string
    # \s*    - Any number of whitespace characters
    # \d+    - One or more digits
    # \s*    - Any number of whitespace characters
    # [-+\/*%] - One of the supported operators: +, -, *, /, %
    # \s*    - Any number of whitespace characters
    # \d+    - One or more digits
    # \s*    - Any number of whitespace characters
    # $      - End of the string
    
    return re.match(pattern, expression) is not None

# Testing the function
expressions = [
    "5 + 2",
    "9 * 1",
    "hello world",
    "123",
    "5 + foo",
    "4/2",
    "3 % 2",
    "10 - 7",
    "8 * 4",
]

for expression in expressions:
    print(f"{expression} --> {is_math_expression(expression)}")

print("_________________________________________________") 

# Solution 2
def is_math_expression(expression):
    operators = ['+', '-', '*', '/', '%']
    parts = expression.split()

    # Check if the expression has three parts
    if len(parts) != 3:
        return False

    num1, operator, num2 = parts

    # Check if the operator is supported
    if operator not in operators:
        return False

    # Check if both numbers are integers
    if not num1.isdigit() or not num2.isdigit():
        return False

    return True

# Testing the function
expressions = [
    "5 + 2",
    "9 * 1",
    "hello world",
    "123",
    "5 + foo",
    "4/2",
    "3 % 2",
    "10 - 7",
    "8 * 4",
]

for expression in expressions:
    print(f"{expression} --> {is_math_expression(expression)}")

print("_________________________________________________") 

# Solution 3
import re

def is_math_expression(expression):
    pattern = r"^\s*\d+\s*[-+\/*%]\s*\d+\s*$"
    return bool(re.match(pattern, expression))

# Testing the function
expressions = [
    "5 + 2",
    "9 * 1",
    "hello world",
    "123",
    "5 + foo",
    "4/2",
    "3 % 2",
    "10 - 7",
    "8 * 4",
]

for expression in expressions:
    print(f"{expression} --> {is_math_expression(expression)}")
