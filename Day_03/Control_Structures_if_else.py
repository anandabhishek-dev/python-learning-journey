# CONDITIONAL STATEMENTS (IF / ELIF / ELSE)

# Example 1: Movie Ticket Eligibility

ticket_price = 90
wallet_size = 100

# Shortcut:
# Ctrl + Enter (Run)

if ticket_price <= wallet_size:
    print("Hurrah! You can go to the movie!")
else:
    print("Sorry! You can't go to the movie!")


# Syntax:
# if (condition):
#     code
#
# elif (condition):
#     code
#
# else:
#     code


# Example 2: Grade Calculator

marks = 91

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
else:
    print("FAIL")


# Practice with Gemini

# Practice Question:
# Write a Python program that prints a greeting based on the current hour.
#
# Rules:
# 5–11   : Good Morning!
# 12–17  : Good Afternoon!
# 18–23  : Good Evening!
# 0–4    : Good Evening!
#
# Test with different values such as:
# hour = 9, hour = 14, hour = 20

hour = int(input("Enter the hour (0-23): "))

if 5 <= hour <= 11:
    print("Good Morning!")
elif 12 <= hour <= 17:
    print("Good Afternoon!")
elif (18 <= hour <= 23) or (0 <= hour <= 4):
    print("Good Evening!")
else:
    print("Invalid hour. Please enter a value between 0 and 23.")