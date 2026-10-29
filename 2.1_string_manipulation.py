"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The user enters the sentence "how are you".

# 2. Process:
# Python transforms the sentence using four string methods:
# uppercase, lowercase, title case, and removing extra spaces.

# 3. Out:
# The program displays four different versions of the sentence.

# 4. My four transformations, and when each is useful:
# upper() - I can use it to write a message in capital letters for emphasis.
# lower() - I can use it to keep messages in a consistent lowercase format.
# title() - I can use it to format the beginning of each word in a heading.
# strip() - I can use it to remove unwanted spaces from user input.



# Your code below

sentence = input("Enter a sentence: ")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Without outer spaces:", sentence.strip())

#output

#Enter a sentence: how are you
#Uppercase: HOW ARE YOU ?
#Lowercase: how are you ?
#Title case: How Are You ?
#Without outer spaces: how are you ?
