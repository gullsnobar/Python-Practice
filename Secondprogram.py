# Strings
# In Python, a string is a sequence of characters enclosed within quotes.

string1 = 'Gull'
string2 = "Snobar"
string3 = """Amjad"""
output = string1+string2+string3
print(output);

# Common String Operations
# 1)- Concatenation: Combining strings using the + operator.

str1 = "Hello"
str2 = "World"
FinalResult = str1 + "," + str2 + "!"
print(FinalResult)

greeting = "Hello"
name = "Snobar"
message = greeting + "," + name
print(message)

# 2)- Repetition: Repeating a string using the * operator.

laugh = "ha"
print(laugh*3)

baba = "ba"
print(baba*2)

# 3)- Indexing: Accessing individual characters in a string using indices.

text = "Python"
print(text[0])
print(text[-1])

# 4)- Slicing: Extracting a substring using slicing.

text = "GULLSNOBAR"
print(text[0:4])
print(text[4:10])

# 5)- Length: Finding the length of a string using len().

Name = "Amjad"
print(len(Name))

name1 = "gull"
print(len(name1))

# 6)- Membership: Checking if a substring exists in a string using in.

myname = "muhammad"
print("hammad" in myname)

myname1 = "tayyab"
print("tayyab" in myname1)

# 7)- String Methods: Python provides many built-in methods for string manipulation.

text = "    Muhammad  Tayyab   "
print(text.strip())
print(text.lower())
print(text.upper())
print(text.split())

# 8)- Escape sequences are used to include special characters in strings.

name = "shafaq\n Amjad"
print(name)

name = "shafaq\t Amjad"
print(name)

print('It\'s a sunny day.')
print('my name\'s a snobar')


#  Python strings are Unicode by default, allowing you to work with characters from any language.

text = "Guten Abend"
print(text)

greet = "aishiteru"
print(greet)