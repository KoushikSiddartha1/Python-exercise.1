"""
Exercise 3.0 — Basic Arithmetic

1. In:
The user enters two numbers.

2. Process:
Python performs addition, subtraction,
multiplication and division.

3. Out:
The program displays the results of all four operations.

4. What happens when the second number is zero, and why:
The program displays a message instead of dividing by zero,
because division by zero is mathematically undefined.
"""

# Ask the user to enter two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Addition
addition = number1 + number2
print("Addition:", addition)

# Subtraction
subtraction = number1 - number2
print("Subtraction:", subtraction)

# Multiplication
multiplication = number1 * number2
print("Multiplication:", multiplication)

# Division
if number2 == 0:
    print("Division is not possible because the second number is zero.")
else:
    division = number1 / number2
    print("Division:", division)

# CHECK IT YOURSELF:
# Test with 7 and 2.
# Expected: addition = 9, subtraction = 5,
# multiplication = 14, division = 3.5.
# Then test with 7 and 0.
# Division should display an error message.

#output :-
"""
Enter the first number: 7
Enter the second number: 2
Addition: 9.0
Subtraction: 5.0
Multiplication: 14.0
Division: 3.5
"""
