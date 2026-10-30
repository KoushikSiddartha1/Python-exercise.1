
"""
Exercise 5.1 — For Loops

1. In:
A list containing the expected returns of eight investment projects.

2. Process:
Python loops through every return in the list.
For each item, it calculates its percentage share
of the total returns and identifies its position.

3. Out:
The program displays each investment return,
its position and its percentage share of the total.

4. What I compute for each item, and why it is worth showing:
I calculate the percentage share of each return
because it helps compare each project's contribution
to the total returns in the list.
"""

# List from Exercise 4.0
returns = [8, 12, 6, 15, 10, 9, 14, 11]

# Calculate the total of all returns
total_returns = sum(returns)

# Loop through every item in the list
for position, value in enumerate(returns, start=1):

    # Calculate the percentage share of each return
    percentage = (value / total_returns) * 100

    # Display the position, return and percentage
    print(
        "Position:", position,
        "| Return:", value, "%",
        "| Share of total:", round(percentage, 2), "%"
    )

# CHECK IT YOURSELF:
# The original list contains 8 items.
# The program should print exactly 8 lines.
# Check that the positions run from 1 to 8.
# Check that the total returns equal 85.
