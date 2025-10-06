python practise w3schools

# indentation 
if 5 > 2:
    print("Five is greater than two!")

# variables 
x = 5 # here we have attached the integer value of 5 to the variable x
y = "Hello, World!" # have attached the string hello world to the variable y 

# we can also assign multiple values to a single variable as seen below
x = y = z = "Orange"
print(x)
print(y)
print(z)

# we can unpack a list as well
fruits = ["apple", "banana", "oranges"]
x,y,z = fruits 
print(x)
print(y)
print(z)

# if we want to output variables 

x = "python is awesome"
print(x) # the print function allows us to do that and will the give us the string values assigned to the variable x 

# to put a global variable within a function we have to literally call it global 

def myfunc():
    global x 
    x = "fantastic"

myfunc()
print("Python is", + x )

# list and a tuple 
x = ["apple", "banana", "pear"]
x = ("apple", "banana", "pear")

# this shows how to create a dictionary 
person = {
    "name":  "Ben",
    "age" : 30,
    "city": "York"

} 

# now if we want to access one of these values we do this 

print(person["name"]) # as a result this will print us the value of the person name which in this case is ben

# there are 3 numeric data types in python 
int float and complex 

x = 1 # int    
x = 1.1 # float     
x = 1j # complex 

# if we want to identify the type of teach we do 

print(type(x))
print(type(x))
print(type(x))

# if we want to convert from one data type to another we do this and assign the value to another variable 

# convert from int to float 
a = float(x)

# convert from the float to complex 
b = complex(x)

print(a)
print(b)

# cannot convert complex data types into another data type 

# if we want to generate a random number between a given range we use the in built random module to do so 
import random 
print(random.randrange(1, 10))

# this will in turn generate a random number between 1 and 10 

person : {
    "name" : "ben",
    "age" : 30,
    "city" : "York"

}

# this section will focus on strings 

# strings are surrounded by either single '' or double " quotation marks
eg "hello"
# to assign a string to a variable 

a = "Hello"

# strings as arrays 
a = "Hello, World"
print(a[1]) # this will print of the letter e as remember in arrays the first character, in this case h, has the position 0 

# strings themselves are arrays 
# if we want to loop through a string we do this 

for x in "apple": 
    print(x) #  this will go through each letter one by one and assign it to the variable x 

# if we want the length of a string we use the len() function 

a = "Hello, World"
print(len(a))

# slicing strings 
# this is used to return a range of characters by using the slice syntax 
# pretty much to return a certain character from a string

b = "Hello, World"
print(b[2:5]) # this will give everything from the 2nd posiion character (l) up to and not inclding the 5th character (4th) - (o)
# so this would return llo

# if we want to do negative indexing then we do
# the rule is that the position starts at -1 on the right hand side of the string 

b = "Hello, World!"
print(b[-5:-2])

# ! is -1 and doing this slice will give us o from -5 to but not including the -2 position which would be l which is -3

# now we look on to modifying strings 
# we can use the upper() to return the string in upper case 

a = "Hello, World"
print(a.upper())

# vice versa for lower case 

a = "Hello, World"
print(a.lower())

# string concatenation 
# this just means to combine, we use the + operator 

a = "Hello"
b = "World"
c = a + b 
print(c)
# this will just give HelloWorld 

# to give a space between them just do 

c = a + " " + b 

# we can't combine strings and numbers together and assign to a variable 
# we can use f strings to do this 

age = 36 
txt = f"My name is John, I am {age}"
print(txt)

# we use {} as placeholders for variables and other operations in case as part of f strings

distance  = 60 
journey = f"We are {distance} miles away from Saturn"

# if we want to further modify our strings we can use the :.2f - this means fixed point number rounded to 2 decimal points (2dp)

# an example is given below 

price = 59 
txt = f"The price of the banana is {price:2f} dollars"
print(txt)

# boolean represent one of two values True or False 

# when evaluating any two values in the python, we can run statements through and get a response 

print(10 > 9)
print(10 == 9)

# we can combine this with if and else loops 

a = 300 
b = 200

if b > a:
    print("b is greater than a")
else:
    print("b is smaller than a")


# now we go onto lists 
# we use [] for lists
# lists are changeable and ordered, meaning we can change, add and remove items in a list after it has been created, lists also allow duplicates 


myList = ["apple", "banana", "cherry"]
print(myList)

# just like in arrays, the the first item in lists has the index [0]

# if we want to find the length of the a list just use the 

len() # just the len function 

print(len(myList))

# lists can be of any data types (string,integeer and boolean)

# we are going to show how to access lists 
# if we want to access the third item of the list above

print(myList[2])
# this should in turn give us the value "cherry"

# just like in arrays for negative indexing we start from -1 on the left most side 

# so to print of the middle item in the list we do 
print(myList[-2])

# this should return us the value of "apple"

# just like with arrays, we also slice through lists with a range 

myList = ["apple", "banana", "cherry", "strawberry", "pear","orange"]
print(myList[2:5])
 
# same for negative indexing 

# we can check if a item exists
myList = ["apple", "banana", "cherry", "orange", "pear","orange"]
# to check we can use a if loop and in 

if "apple" in myList: 
    print("Yes, 'apple' is in the fruits list")

# if we want to change the value of a specific item, we can refer to the index number 

myList = ["apple", "banana", "cherry", "orange", "pear","orange"]
myList[0] = "blueberry"
print(myList)

# if want to change a range of item values we just do the same inputting the range which we want 

myList[1:2] = ["pineapple", "mango"]
print(myList)

# to add an item to the end of the list we can use the append() method

myList = ["apple", "banana", "cherry", "orange", "pear","orange"]
myList.append("Orange")
print(myList)

# to add elements from 1,2another list to the current list use the .extend() method

# to remove an item from a list we do 
myList = ["apple", "banana", "cherry", "orange", "pear","orange"]
myList.remove("apple")

# to clear the entire list 
# we use the clear() function 

myList = ["apple", "banana", "cherry", "orange", "pear","orange"]
myList.clear()
print(myList)


# we can also loop through a list 
myList = ["apple", "banana", "cherry", "orange", "pear","orange"]
for x in myList:
    print(x) #  this will run through all the items in the list one by one 

# can also do the same thing using the range() and len() function 

myList = ["apple", "banana", "cherry", "orange", "pear","orange"]
for i in range(len(myList)): 
    print(myList[i])

# we can also run the list items through a while loop 

thislist = ["apple", "banana", "cherry"]
i = 0
while 1 < len(myList):
    print(myList[i])
i = i + 1 

# comprehension is when we want to create a new list 
newlist = []

# now we go into tuples 

# to unpack tuples we assign a element to a variable like below 
fruits = {"apple", "banana", "pear", "mango"}
(purple, yellow, greeb, blue) = fruits 
print(purple)
print(green)
print(yellow)

# for loops, just like lists and sets 
fruits = ("apple", "banana", "pear", "mango")
for x in fruits:
    print(x) # this will loop through all the values in the fruits tuple 

# just like lists and sets we can also loop through all the indices, rememeber the range of the length of the tuple

fruits = ("apple", "banana", "pear", "mango")
for i in range(len(fruit)):
    print(fruit[i])

# we can add items to a set by using the .add() method, remember sets are written in {}

fruits = {"apple", "banana", "pear", "mango"}
fruits.add("orange") # this adds "orange" to the set

print(fruits)

# to add items from one set to another we use the .update() module, with lists we use the .extend module 

# the object in the update()  method does not need to be a set as well, it can be a tuple, dictionary or list 

# if we want to remove a item from a set just use .remove() module to do so 

fruits = {"apple", "banana", "pear", "mango"}
fruits.remove("apple")
print(fruits)

# can also use .discard() to remove a item from a list, will not raise a error if the item does not exist unlike .remove() which will 

# if want to remove a random item can use .pop() module

# the .clear() module empties the set 

# del will delete the set completely

# if want to join sets we use the .union module 

# it will return a new set with all items from both sets

set1 = {"a", "b", "c"}
set2 = {"a", "b", "c"}

set3 = set1.union(set2)
print(set3) #  remember to always print off the remaining function to actually see the items printed off

# if want to join multiple sets, let's say we have 4 sets 

myset = set1.union(set2, set3, set4)
print(myset)


# the .union() allows to join a set with a tuple 

# the difference between .union() and the .update() module is that the .update() moves all the items from one set into another, it does not return a new set 
set1 = {"a", "b", "c"}
set2 = {"a", "b", "c"}

set1.update(set2)
print(set1)

# we will have a look at the .intersection() method
# this method will return a new set but only with items that are present in both sets , remember returns a new set 
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "pear", "mango"}

set3 = set1.intersection(set2)
print(set3) # this will return the duplicate value of "banana"


# we can alao use the .difference() method 

# this method will return a new set that will contain only the items from the first set that are not present in the second set 
set1 = {"apple", "mango", "banana", "orange", "pear"}
set2 = {"pear","orange", "pineapple"}

set3 = set1.difference(set2) 
print(set3) # this will give us the values "mango", "apple" , "banana" as these are not in set2

# now we move onto dictionaries 
# they are used to store data values in key : value pairs 
# it is a collection which is ordered, changeable and do not allow duplicates 

# they are of the form 

person : {
    "Name" : "Ben",
    "City" : "London", 
    "Age" : 30 
} 
print(person)

# if want to output a certain value within the dictionary we do 
print(person[Age]) # this will output the integer value 30 

# to find out how many items a dictionary has, we use the len () function 
print(len(person)) # this will tell us that there are 3 items in the dictionary labelled "person"

# the values in dictionaries can be of any data type 

# dictionaries are defined as objects with data type "dict"

# if want to access a item we can assign it to a variable x 

x = person["Age"]
# can also use the .get() function to carry out the same process 

x = person.get("Age")

# the .keys() function will return all the keys in the dictionary 

x = person.keys() 

# if we want to add a new item to the dictionary we do 

x = person.keys()

print(x)
person["Pet"] = "Cat" 

print(x)

# just like with .keys() the .values() function will return all values in the dictionary

x = person.values()

# the .items() function will return each of the items in a dictionary as tuples in a list 

x = person.items()

# this will give us 
[('Name', 'Ben'), ('City', 'London'), ('Age', '30')]

# now we move onto numpy 

# it is a python library, short for "numerical python"

 # Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

# to use numpy we do 

import numpy 

# to create arrrays with numpy 

# the array object is called ndarray , just the name for a array but in numpy 

# to create array in numpy, we use the np.array() function 

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# so the above was a list 

# we can do the same for a array in the form a tuple 

import numpy as np 
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# there are different types of arrays which have different number of dimensions 

# we will start with 1-D arrays, these are the basic arrays 

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# now we will move onto 2d arrays, these just contain two arrays within the brackets

import numpy as np 
arr = np.array([[1,2,3], [4, 5, 6]])
print(arr)

# now we will move onto 3d arrays, these contain two pairs of 2d arrays 

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]])
print(arr) 






     














