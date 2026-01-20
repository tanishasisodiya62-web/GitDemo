# task 1: Basic mathematics operation

# Taking input from user

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Not possible (divide by zero)"

# Displaying results
print("The sum is: ", addition)
print("The difference is: ", subtraction)
print("The multiplication is: ", multiplication)
print("The division is: ", division)







# Task 2:  Greetings

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print("hello " + full_name + "! Welcome to Python program.")
# first_name = input("Enter your first name: ")