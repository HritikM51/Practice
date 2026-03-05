# =========================================
# PYTHON PRACTICE
# LEVEL 1 — SET 1
# Questions 1 – 6
# =========================================


# --------------------------------------------------
# Question 1
# Print the following exactly:
# Python Practice Started
# Day 1
# I will master Python
# --------------------------------------------------

print("Python Practice Started")
print("Day 1")
print("I will master Python")


# --------------------------------------------------
# Question 2
# Situation:
# You are building a movie ticket system.
# Print the following message when the program starts:
#
# Welcome to MovieHub
# Ticket booking system started
# Enjoy your show
# --------------------------------------------------

print("Welcome to MovieHub")
print("Ticket booking system started")
print("Enjoy your show")


# --------------------------------------------------
# Question 3
# Output Prediction
# What will be the output of the following code?
#
# print("Python")
# print("Practice")
# print()
# print("Day 1")
# --------------------------------------------------

print("Python")
print("Practice")
print()
print("Day 1")


# --------------------------------------------------
# Question 4
# Debug the following code.
# Fix the syntax errors.
#
# print("Learning Python)
# print(Python is powerful)
# --------------------------------------------------

print("Learning Python")
print("Python is powerful")


# --------------------------------------------------
# Question 5
# Variables Practice
# Create variables:
# name = John
# country = India
#
# Print exactly:
# Name: John
# Country: India
# --------------------------------------------------

name = "John"
country = "India"

print("Name:", name)
print("Country:", country)


# --------------------------------------------------
# Question 6
# Numbers + Variables
# Create two variables:
# a = 10
# b = 20
#
# Print their sum.
# Expected output:
# 30
# --------------------------------------------------

a = 10
b = 20

print(a + b)

# --------------------------------------------------
# Question 7
# Numbers - Variables
# Create two variables:
# a = 10
# b = 20
#
# Print their difference.
# Expected output:
# 10
# --------------------------------------------------

a = 10
b = 20

print(b - a)


# --------------------------------------------------
# Question 8
# Numbers * Variables
# Create two variables:
# a = 10
# b = 20
#
# Print their product.
# Expected output:
# 200
# --------------------------------------------------

a = 10
b = 20

print(a * b)

# --------------------------------------------------
# Question 9
# Numbers / Variables
# Create two variables:
# a = 10
# b = 20
#
# Print their product.
# Expected output:
# 2
# --------------------------------------------------

a = 10
b = 20

print(b // a) # // , it is called floor division  is used for integer division, which gives the quotient without the remainder.
              # If you want to get the result as a float, you can use the regular division operator (/):
              # print(b / a)



a = 10
b = 2

print(a / b) # / is used for regular division, which gives the quotient as a float, even if both operands are integers.
             # If you want to get the result as an integer, you can use the floor division operator (//):
             # print(a // b)

#--------------------------------------------------
# Question 10
# user input
# Ask the user to enter their name and print a greeting message.    

print("Program started")

name = input("Enter name: ")

print("You entered:", name)

print("Program ended")

#--------------------------------------------------
# Question 11
#Concept: Taking User Input with input()

variable = input("message : ")      
print(variable)
print(variable , name) 

#--------------------------------------------------
# Question 12
# Concept: Taking User Input with input() and String Concatenation
name = input("Enter your name: ")
print("Hello, " + name + "!")

#--------------------------------------------------

# Question 13
#consept : input() always returns text (string), but for math operations we need numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print("The sum is:", result)

#--------------------------------------------------
# Question 14
#consept : When we take numbers from the user using input(), they are strings (text). To perform math operations, we need to convert them to integers using int().
num1 = int(input("Enter number: "))
print(num1 *2)

#--------------------------------------------------
# Question 15
# We can combine text + user input to create dynamic messages.
name = input("Enter name: ")

print("Hello", name)  

#different ways to print the same message
print("Hello " + name) # string concatenation means combining strings using the + operator
print("Hello {}".format(name)) # The format() method is a string method that allows you to insert values into a string using placeholders ({}).
print(f"Hello {name}") # f-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces {}. They are prefixed with 'f' or 'F' before the opening quotation mark.

#--------------------------------------------------
#Question 16
# consept : Ask the user to enter their name. Then, print a personalized greeting message using f-strings.
name = input("Enter name: ")    
print(f"Hello {name}, welcome to Python practice!")
#--------------------------------------------------
#Question 17
