# print statement

print("My name is Gull Snobar." , "I am 20 years old")
# print("I am 20 years old")

print(45+89)

# Variables

name = "Snobar"
age = "34"
price = "78.79"

print(name)
print("My name is:" , name)

print(type(name))
print(type(price))

# string

name1 = 'gull'
name2 = "gull"
name3 = '''gull'''

print(name1)
print(name2)
print(name3)

# Datatypes
# There are 5 datatypes in python

# 1- Integers (+ve or -ve numbers)
# 2- String ("Snobar")
# 3- Float 9.67
# 4- Boolean (True or False)
# 5- None

num = 67
print(num)

name4 = "GULLSNOBAR"
print(name4)

float = 6.98
print(float)

old = True
print(old)

a = None
print(a)

# PrintSum

a = 6
b = 4
sum = a + b
print(sum)

# Comments

# 1 - Single line Comments
# 2 - Multiline Comments

# Types of Operators
# An operator is a symbol that performs a ceratain operation between operands
# 1 - Arithmetic operators

a = 6
b = 7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# 2 - Retional/Comparison Operators

a = 67
b = 56
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# 3 - Assignment Operator

num = 34
num += 45
num **= 5
print("num:", num)

# 4 - Logical Operators (not, and, or)
# Not operator works on single operator

print(not False)
print(not True)

# And/Or operators works on two operators

val1 = True
val2 = True
print("AND Operators:", val1 and val2)
print("OR Operators:", (a==b) or (a>b))

# Type Conversion
# Float is superior as compare to integer

a = 5
b = 6.98 
sum = a + b
print(sum)

# Type Casting
# We use type casting to convert 1 datatype into another datatype

a = int("2")
b = 4.67
sum = a + b
print(sum)
print(type(a))
print(type(b))

# Inputs

# input("Enter your name:")
# name = input("Enter your age:")
# print(name)

# val = int(input("Enter some value:"))
# print(type(val), val)

# First Program
# first = int(input("Enter your 1st number:"))
# second = int(input("Enter your 2nd number:"))
# print("Sum:", first + second)

# Second Program
# WAP to input size of a square and print its area

# side = int(input("Enter your side: "))
# print("Area =" , side * side)

# Third Program

a = float(input("Enter 1st num: "))
b = float(input("Enter sec num: "))

print("Avg =", (a+b)/2)


