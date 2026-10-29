"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""


"""
1. In:
The program starts with information about a corporate investment project.

2. Process:
Python stores the project details in a dictionary, reads a field,
changes its value, removes one field, and displays all remaining
fields with their values. It also handles a field that does not exist.

3. Out:
The program displays the original project details, an updated value,
a message for the missing field, and all remaining fields.

4. My object and fields:
I described a corporate investment project.
The fields are project_name, investment_amount, expected_return,
risk_level, and duration_years. These help evaluate an investment's
cost, expected profitability, risk, and time horizon.
"""

# Create a dictionary describing a corporate investment project
project = {
    "project_name": "Solar Energy Expansion",
    "investment_amount": 500000,
    "expected_return": 12,
    "risk_level": "Medium",
    "duration_years": 5
}

# Display the original dictionary
print("Original project:", project)

# Read one field
print("Expected return:", project["expected_return"], "%")

# Change the expected return
project["expected_return"] = 14
print("Updated expected return:", project["expected_return"], "%")

# Check a field that does not exist
missing_field = project.get("discount_rate")

if missing_field is None:
    print("The discount_rate field does not exist.")

# Remove one field
project.pop("risk_level")

# Display every remaining field and its value
print("\nFinal project details:")
for field, value in project.items():
    print(field, ":", value)

# CHECK IT YOURSELF:
# Accessing project["discount_rate"] directly raises a KeyError
# because the field does not exist.
# Using project.get("discount_rate") returns None instead,
# allowing the program to handle the missing field safely.

#output
"""
Original project: {'project_name': 'Solar Energy Expansion', 'investment_amount': 500000, 'expected_return': 12, 'risk_level': 'Medium', 'duration_years': 5}
Expected return: 12 %
Updated expected return: 14 %
The discount_rate field does not exist.

Final project details:
project_name : Solar Energy Expansion
investment_amount : 500000
expected_return : 14
duration_years : 5 """