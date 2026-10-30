"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""
"""
1. In:
The program uses my original list of eight expected investment returns
from Exercise 4.0.

2. Process:
Python displays the returns in four different orders:
ascending, descending, reversed, and randomly shuffled.
Some operations create a new list, while others modify the original.

3. Out:
The program displays the four different arrangements and finally
displays the original list to prove that it has not changed.

4. My four orders, and which ones modify the original:
sorted() - Arranges returns in ascending order without changing the original.
sorted(reverse=True) - Arranges returns in descending order without changing the original.
reversed() - Displays the returns in reverse order without changing the original.
shuffle() - Randomly rearranges the original list itself.
"""

# Import random module
import random

# Original list from Exercise 4.0
returns = [8, 12, 6, 15, 10, 9, 14, 11]

# Display original list
print("Original investment returns:", returns)

# 1. Ascending order (new list)
ascending = sorted(returns)
print("Ascending order:", ascending)

# 2. Descending order (new list)
descending = sorted(returns, reverse=True)
print("Descending order:", descending)

# 3. Reverse order (new list)
reverse_order = list(reversed(returns))
print("Reverse order:", reverse_order)

# 4. Random order (copy first to protect original)
random_order = returns.copy()
random.shuffle(random_order)
print("Random order:", random_order)

# Final check: display the original list
print("Original list after all operations:", returns)

# CHECK IT YOURSELF:
# My original list in Exercise 4.0 was:
# [8, 12, 6, 15, 10, 9, 14, 11]
# After performing all four operations, I display the original list.
# I checked all eight values one by one.
# The values are in the same order as Exercise 4.0.
# Therefore, my original list has not been modified.

#output :-
"""Original investment returns: [8, 12, 6, 15, 10, 9, 14, 11]
Ascending order: [6, 8, 9, 10, 11, 12, 14, 15]
Descending order: [15, 14, 12, 11, 10, 9, 8, 6]
Reverse order: [11, 14, 9, 10, 15, 6, 12, 8]
Random order: [8, 11, 9, 15, 14, 6, 10, 12]
Original list after all operations: [8, 12, 6, 15, 10, 9, 14, 11]
Final original list: [8, 12, 6, 15, 10, 9, 14, 11]
"""