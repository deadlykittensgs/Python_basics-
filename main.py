
# Basic Function using indention 
this_line = True


def my_function():
  print("Hello from a function")




  # For loop and while loop 

# Use for loops when you have a defined number of interations 
# While loop to interate until a condition is met 



# Basic "for" loop 
# "x" is the thing you are on and "fruits" is the array or object. you tell the function what to to dith x int the for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# basic "while" loop based on a variable 

while this_line == True:
  print(f"here is a formated string {fruits[1]}")  
  break

count = 5
# counting up in a while loop 
while count < 10:
  print(f"here is a formated string {fruits[0]}")
  count = count + 1  

# Lists (arays in Python)

my_list = [1, 2, 3, 4, 5]

# Dictionary syntax

my_dict = {
    "name": "Ryan",
    "age": 25,
    "is_student": False
}

# Access data in a dictionary

print(my_dict["name"])   # Output: Ryan


# use get to avoid null errors 
print(my_dict.get("email"))  # Output: None


my_dict["age"] = 26             # Update value
my_dict["email"] = "a@b.com"    # Add new key-value pair
del my_dict["is_student"]       # Remove a key

for key, value in my_dict.items():
    print(f"{key}: {value}")


# Basic funtions included in the language 


append()	#Adds an element at the end of the list
clear()   #Removes all the elements from the list
copy()	  #Returns a copy of the list
count()   #Returns the number of elements with the specified value
extend()	#Add the elements of a list (or any iterable), to the end of the current list
index()	  #Returns the index of the first element with the specified value
insert()	#Adds an element at the specified position
pop()	    #Removes the element at the specified position
remove()	#Removes the first item with the specified value
reverse()	#Reverses the order of the list
sort()	   #Sorts the list



and	          # A logical operator
as	          # To create an alias
assert	      # For debugging
break         # To break out of a loop
class	        # To define a class
continue	    # To continue to the next iteration of a loop
def	          # To define a function
del	          # To delete an object
elif	        # Used in conditional statements, same as else if
else	        # Used in conditional statements
except	      # Used with exceptions, what to do when an exception occurs
False	        # Boolean value, result of comparison operations
finally	      # Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	          # To create a for loop
from	        # To import specific parts of a module
global	      # To declare a global variable
if	          # To make a conditional statement
import	      # To import a module
in	          # To check if a value is present in a list, tuple, etc.
is	          # To test if two variables are equal
lambda	      # To create an anonymous function
None	        # Represents a null value
nonlocal	    # To declare a non-local variable
not           #	A logical operator
or	          # A logical operator
pass	        # A null statement, a statement that will do nothing
raise	        # To raise an exception
return	      # To exit a function and return a value
True	        # Boolean value, result of comparison operations
try	          # To make a try...except statement
while	        # To create a while loop
with	        # Used to simplify exception handling
yield	        # To return a list of values from a generator