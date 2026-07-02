# DAY 04 - LOOPS & FUNCTIONS


# ==========================
# FOR LOOP
# ==========================

# Syntax:
# for iterator in range(start, end):
#     code

# 'i' is called an iterator (any valid variable name can be used).
# range(start, end) works till end-1.
# By default, the start value is 0.
# Example: range(11) prints numbers from 0 to 10.

for i in range(1, 101):
    print(i)


# ==========================
# PRINT MULTIPLES OF 10
# ==========================

for i in range(1, 101):
    if i % 10 == 0:
        print(i)
    else:
        continue


# ==========================
# WHILE LOOP
# ==========================

i = 0

while i < 10:
    print(i + 1)
    i += 1


# ==========================
# FUNCTIONS
# ==========================

# Function that prints the sum

def add(x, y):
    print(x + y)


add(4, 5)


# Function that returns the sum

def sum(a, b):
    return a + b


result = sum(3, 5)

print(result)