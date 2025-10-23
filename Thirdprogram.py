# Example 1: Check the value of a variable and print a message
x = 10

if x > 20:
    print("x is greater than 20")
elif x > 15:
    print("x is greater than 15 but less than or equal to 20")
elif x > 10:
    print("x is greater than 10 but less than or equal to 15")
else:
    print("x is less than or equal to 10")

# Example: 2
# Another Example: Check if a Number is Positive, Negative, or Zero

num = -5

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Example: 3
# Calculate the grade based on a score

score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
elif score >= 50:
    print("Grade F")
else:
    print("Fail")


# For Loop

# 1. looping over a range of numbers

for i in range(10):
 print(i)

# 2. looping through a list

fruits = ["apple", "mango", "orange"]
for fruit in fruits:
    print(fruit)

# 3. Looping through characters in a string:
word = "Gangster"
for char in word:
    print(char)

# 4. Using a for loop with range() for a specific step:

for i in range(0 , 20, 2):
    print(i)
# start from 0 and ends with 20 but 20 is exclude

for i in range(0 , 12, 3):
    print(i)