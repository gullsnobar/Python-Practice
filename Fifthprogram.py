# Dictionary in Pythons
# A dictionary is a collection of key-value pairs.

dic = {
    "name": "Gull Snobar",
    "age": "21",
    "marks": 90.6,
    "semester": 6,
    "University": "University of Education",
}
print(dic);

# accessing any index

print(dic["name"]);
print(dic["age"]);
print(dic["marks"]);

# Adding a new key-value pair

stu = {
    "University": "Education University"
}
stu["University"] = "Oxford University";
print(stu);

# Sets
# A set is an unordered collection of unique elements.
# It is mutable but cannot have duplicate values.

fruits = {'apple', 'banana', 'cherry'}
print(fruits)

# Sets Methods

# add element
set = {1,2,3,4,5}
set.add(6);
print(set);

# add element
set = {"helo", "world"}
set.add("Universe");
print(set);

# update element
set = {1,2,3,4,5}
set.update([6,7,8]);
print(set);

# remove element
set = {6,7,7,9,0, "hello"}
set.remove("hello");
print(set);

# discard an element
set = {6,7,7,9,0, "hello"}
set.discard(7);
print(set);

# Important methods of Sets

# Union 

A = {1,8,5,9}
B = {1,3,9,6,0}
print(A.union(B));
# another way to print
# print(A|B);

# Intersection

A = {6,7,8,9,10}
B = {1,2,3,4,5,6}
print(A.intersection(B));
# another way to print
# print(A&B);

# Difference

A = {1,2,3,4}
B = {1,2,3,4}

print(A.difference(B));