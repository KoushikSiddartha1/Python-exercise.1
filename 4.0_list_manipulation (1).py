"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""
"""
1. In:
The program uses a list of expected returns from eight corporate
investment projects.

2. Process:
Python displays the list, selects one return, sorts the returns
from lowest to highest, and calculates their average.

3. Out:
The program displays all eight returns, one selected return,
the sorted returns, and the average expected return.

4. What my list is about, and what I computed from it:
My list represents expected returns on corporate investments.
I calculated the average return to understand the overall
expected performance of these investment projects.
"""


# Your code below

# Create a list of expected returns (percentages)
returns = [8, 12, 6, 15, 10, 9, 14, 11]

# Display the complete list
print("Expected investment returns (%):", returns)

# Display one item: the first project's expected return
print("First project's expected return:", returns[0], "%")

# Display returns sorted from lowest to highest
print("Sorted returns (%):", sorted(returns))

# Calculate and display the average expected return
average_return = sum(returns) / len(returns)
print("Average expected return:", round(average_return, 2), "%")


# Self-check:
# First three returns are 8%, 12%, and 6%.
# Manual total: 8 + 12 + 6 = 26.
# Manual average: 26 / 3 = 8.67%.
# I can compare this result with Python's calculation.
returns = [8, 12, 6, 15, 10, 9, 14, 11]
first_three = returns[:3]
check_average = sum(first_three) / len(first_three)

print("Average of first three returns:", round(check_average, 2), "%")

#output 
""" Expected investment returns (%): [8, 12, 6, 15, 10, 9, 14, 11]
First project's expected return: 8 %
Sorted returns (%): [6, 8, 9, 10, 11, 12, 14, 15]
Average expected return: 10.62 %
Average of first three returns: 8.67 %"""

