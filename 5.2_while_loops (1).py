
"""
Exercise 5.2 — While Loops

1. In:
The user enters an answer.

2. Process:
Python repeatedly asks the user to type yes.
The program checks the answer and counts the attempts.

3. Out:
The program displays whether the user entered
the correct answer and provides a summary.

4. My stop condition, my attempt limit, my summary:
The program stops when the user enters yes.
The maximum number of attempts is 3.
The summary displays the total attempts
and whether the user succeeded.
"""

# Set the expected answer
expected_answer = "yes"

# Set the maximum number of attempts
maximum_attempts = 3

# Start the attempt counter
attempts = 0

# Track whether the user entered the correct answer
success = False

# Repeat while the answer is incorrect and attempts remain
while attempts < maximum_attempts and success == False:

    # Ask the user for an answer
    answer = input("Type yes to confirm: ")

    # Remove extra spaces and convert to lowercase
    answer = answer.strip().lower()

    # Increase the attempt counter
    attempts += 1

    # Check whether the answer is correct
    if answer == expected_answer:
        print("Correct! You have confirmed successfully.")
        success = True
    else:
        print("Incorrect answer. Please try again.")

# Display the summary
print("\n--- SUMMARY ---")
print("Total attempts:", attempts)

if success:
    print("Result: Successful")
else:
    print("Result: Maximum attempts reached. Program stopped.")

# CHECK IT YOURSELF:
# Test by entering an incorrect answer three times.
# The program should stop after exactly 3 attempts.
# Test again using YES, Yes or " yes ".
# These should all be accepted as correct answers.

#output :-
"""
Type yes to confirm: yes
Correct! You have confirmed successfully.

--- SUMMARY ---
Total attempts: 1
Result: Successful

Type yes to confirm: no
Incorrect answer. Please try again.
Type yes to confirm: no
Incorrect answer. Please try again.
Type yes to confirm: ni
Incorrect answer. Please try again.

--- SUMMARY ---
Total attempts: 3
Result: Maximum attempts reached. Program stopped.
"""
