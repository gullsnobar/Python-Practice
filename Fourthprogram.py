
# Lists in Python:
# Definition: A list is a mutable (changeable) ordered collection of items.
# Syntax: Written with square brackets [ ].
# key Points
# You can add, remove, or change items.
# Lists can contain different data types (integers, strings, booleans, etc.).

my_lists = [1,2,3,4, "apple", True, "snobar"];
print(my_lists);

list = [1,2,3,4,5]
print(list);

fruits = ["apple", "cherry", "banana", "orange", "mango"]
print(fruits);

# adding an item

fruits.append("graphes");
print(fruits);

# changing an item 

fruits[1] = "blueberry";


# removing an item
fruits = ["apple", "cherry", "banana", "orange", "mango"];
fruits.remove("cherry");
print(fruits);


# Tuples in Python:
# Definition: A tuple is an immutable (unchangeable) ordered collection of items.
# Syntax: Written with parentheses ( ).
# Key Points:
# You cannot add, remove, or change items after creation.
# Tuples can also contain different data types.
# Tuples are faster and memory efficient compared to lists.

my_tuple = (1,2,3,4,5, "Snobar", True, False);
print(my_tuple);

# creating tuple

colors = ("red", "blue" "green", "white");
print(colors);

# accessing items

print(colors[0]);
print(colors[1]);
print(colors[2]);

# Tuple with one item (important)

one_item_tuple = ("applee",);
print(one_item_tuple);
print(type(one_item_tuple));
