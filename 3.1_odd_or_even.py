
"""
Exercise 3.1 — Odd or even

1. In:
The user enters a positive whole number N.

2. Process:
Python checks every number from 1 to N.
It uses the modulus operator (%) to determine
whether each number is odd or even.

3. Out:
The program displays every number and identifies
whether it is odd or even.

4. What happens on 0, on a negative number, on a very large number:
0 - Display an error message and stop.
Negative number - Display an error message and stop.
5000 - Display a message because the maximum limit is 100.
"""

# Ask the user to enter a number
N = int(input("Enter a positive number: "))

# Check the input
if N == 0:
    print("Zero is not allowed. Please enter a positive number.")

elif N < 0:
    print("Negative numbers are not allowed.")

elif N > 100:
    print("Number too large. Please enter a number up to 100.")

else:
    # Check every number from 1 to N
    odd_count = 0
    even_count = 0

    for number in range(1, N + 1):

        if number % 2 == 0:
            print(number, "is Even")
            even_count += 1

        else:
            print(number, "is Odd")
            odd_count += 1

    # Display the summary
    print("\nTotal odd numbers:", odd_count)
    print("Total even numbers:", even_count)

# CHECK IT YOURSELF:
# I tested the program with N = 6.
# It displayed 6 numbers: 3 odd and 3 even.
# I tested 0 and a negative number, and both were rejected.
# I tested 5000, and the program rejected it because it exceeds 100.
# All four test cases behaved as expected.

#output :-
"""
Enter a positive number: 6
1 is Odd
2 is Even
3 is Odd
4 is Even
5 is Odd
6 is Even

Total odd numbers: 3
Total even numbers: 3
"""

