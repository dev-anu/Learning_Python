# Conditions (if,else,elif)
# Write a program to check whether a number is positive, negative, or zero.

num = int(input("Enter a number to check if it is positive or negetive: "))
if num < 0:
    print("Negative")
elif num > 0:
    print("Positive")
else:
    print("Zero")


# Take input of a number and check if it is even or odd.

numInput = int(input("Enter a number to check if even or odd: "))
if numInput % 2 == 0:
    print("Even")
else:
    print("Odd")

# Take a user’s age and print if they are eligible to vote (18+).

age = int(input("Enter the age of the person: "))
if age >= 18:
    print("You have voting rite.")
else:
    print("You are not eligible.")


# Take 3 numbers and print the largest.
numOne = int(input("Enter First Number: "))
numTwo = int(input("Enter Second Number: "))
numThree = int(input("Enter Third Number: "))

if numOne > numTwo and numOne > numThree:
    print("First one is the greatest")
elif numTwo > numOne and numTwo > numThree:
    print("Second one is the greatest")
else:
    print("Third one is the greatest")


# Check if a year is a leap year.
year = int(input("Enter the year: "))
if year % 400 == 0:
    if year % 100 == 0:
        if year % 4 == 0:
            print("Its a leaf year")
        else:
            print("It's not a leaf year")
    else:
        print("It's not a leaf year")
else:
    print("It's not a leaf year")

# Create a program that checks if a number is divisible by 3 and 5.

num = int(input("Enter the number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible")
else:
    print("Non Divisible")

# Write a program to compare two strings for equality.
str_one = input("Enter string one: ")
str_two = input("Enter string two: ")
if str_one == str_two:
    print("are equal")
else:
    print("not equal")


# Ask the user for a password and validate if it matches "Anurag@123".
password = input("Enter the password: ")
if password == "Anurag@123":
    print("You are authorised")
else:
    print("Acess Denied")


# Take a number and check if it’s in the range 10–50.
num = int(input("Enter a number between 10 to 20: "))
if num >= 10 and num <= 20:
    print(f"{num} is beween 10 and 20")
else:
    print("Invalid number")


# Take input of two numbers and a math operation (+, -, *, /) and perform that operation.
num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))
operator = input("Input any operator +,-,%,/,* ")
result = 0

if operator == "+":
    result = num_one + num_two
elif operator == "-":
    result = num_one - num_two
elif operator == "*":
    result = num_one * num_two
elif operator == "/":
    result = num_one / num_two
elif operator == "%":
    result = num_one % num_two
else:
    print("Please choose a valid operator, form the options",
          num_one, operator, num_two)

print(result)
