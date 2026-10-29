"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: We enter the inputs of name and age using input() funtion 

# 2. Process:
# When we run the program we are asked to enter our name and age.
# Python stores the name and age in variables and combines
# the text with the entered values using print() and concatenation.

# 3. Out:
# The program displays the user's name and age in the terminal once seperately and once 
# together in a sentence

# 4. My two fields, and what I would do with them:
# My two fields are name and age. I can use them to personalize
# messages and determine the user's age.

# Your code below

name = input ("Enter your name : ")
age = input ("Enter your age : ")
print ("My name is:",name)
print ("My age is",age)
print ("My name is " + name + " and " + age + " is my age ",)