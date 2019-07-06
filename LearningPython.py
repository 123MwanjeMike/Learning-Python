#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:17:07 2019

@author: mike
"""
# COMMENTS
# This is a single line comment

"""
    This is a
    multi-line comment
"""
print("Hello World")

print("""The Course  will cover
      the following aspects
      interpersonal communication
      Communication for
      """) #We use tripple quotes for large strings

print("Hello"[0]) #Prints a substring of our string

print("Hello"[0:3]) #Prints the substrings as above in a range
print(2)
print(1,2,3,"Hello","Vision")#Prints on the same line


##########################################################
########### VARIABLES & DATA TYPES########################
##########################################################

greeting = "Hello World"
greeting = "Hey Everyone" #re-assigning

print(greeting)

### Data types
myStr = "Hello" #We use this to identify strings in python
myInt = 25 #We use this to identify integers in python
myFloat = 1.3 #We use this to identify Float values in python

myList = [1,2,3,"Yello",1.875] #We use this to identify lists in python
myDict = {"a":1, "b":2, "c":3} #We use this to identify a dictionary in python

print(type(myStr), myStr)
print(type(myInt), myInt)
print(type(myFloat), myFloat)
print(type(myList), myList)
print(type(myDict), myDict)

print(myList[4])
print(myDict["c"])

print(myStr, "World")
greeting = myStr + "_World"
print(greeting)

##########################################################
########### CONDITIONAL STATEMENTS #######################
##########################################################
x = 4

##### If statement
if x < 6:
    print("This is true")

##### If-else statement
x = 7
if x < 6:
    print("This is true")
else:
    print("This is false")

##### Elif
color = "red"

if color == "red":
    print("Color is red")
elif color == "blue":
    print("Color is blue")
else:
    print("Color is not red or blue")

##### Nested if
if color == "red":
    if x < 10:
        print("Color is red and x is less than 10")

##### Logical Operators
if color == "red" and x < 10:
    print("Color is red and x is less than 10")

##########################################################
######################## LOOPS ###########################
##########################################################

people = ["John", "Sarah", "Tim", "Bob", "Mike"]

##### For Loops
for person in people:
    print("Current Person: ",person)
print("\n")

##### Iterate by seq index
for i in range(len(people)):
    print("Current Person: ",people[i])

for i in range(5, 18):
    print(i)

##### While Loop
count = 0
while count < 10:
    print("Count: ", count)
    if count == 5:
        break
    count = count + 1


##########################################################
###################### FUNCTIONS #########################
##########################################################

##### Create a function
def sayHello(times = 1): #def keyword for defining functions
    for i in range(0,times):
        print("Hello ",(i+1))

sayHello(4)

##### Return a value
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(3,7))

def addOneToNum(num):
    num = num + 1
    print("Value inside function: ", num)
    return

num = 5
addOneToNum(num)
print("Value outside function: ", num)


def addOneToList(mylist):
    mylist.append(4)
    print("Value inside function: ", mylist)
    return

mylist = [1,2,3]
addOneToList(mylist)
print("Value outside function: ", mylist)


###############################################################
############### String Functions ##############################
my_str = "Hello World"
print(my_str.capitalize()) ### Capitalizes the first characters of the string
print(my_str.swapcase()) ### Swaps the case in the string
print(len(my_str)) ### Gets length of the string
print(my_str.replace("World", "Everyone")) ### Replaces a given substring in the string
sub = "l"
print(my_str.count(sub)) ### Counts the number of times a substring appears in a string
print(my_str.startswith("H")) ### Boolean to check if string starts with a given substring
print(my_str.endswith("d")) ### Boolean to check if string ends with a given substring
print(my_str.split()) ### Splits the string
print(my_str.find("World")) ### Finds the first occurance position of a given substring in a string
print(my_str.index("World")) ### Works just like the find function above
print(my_str.isalnum()) ### Returns True if the string is all alphanumeric
print(my_str.isalpha()) ### Returns True if the string is all alphabetic
print(my_str.isnumeric()) ### Returns True if the string is all numeric



##########################################################
###################### MODULES #########################
##########################################################

import greetModule ###Imports an entire module with all its functions
greetModule.say_Hello("Mike")

from greetModule import say_Goodbye ###Used to only import a specific element instead of the whole module
say_Goodbye("Mike")


##########################################################
#######################  FILES  ##########################
##########################################################

fo = open("test.txt", "w") ### Used for opening a file in write mode
print("Name: ", fo.name) ### Getting information about the file
print("Is Closed: ", fo.closed) ### Checking if the file is closed
print("Opening Mode: ",fo.mode) ### Getting which mode the file is in
fo.write("I love Python")
fo.close() ### Used for closing the file

fo = open("test.txt", "a") ### Used for opening the file in append mode
fo.write("\nI also like PHP")
fo.close()

fo = open("test.txt", "r+") ### Opening the file in read mode
text = fo.read() ### Read the file
Text = fo.read(10) ### Read the first 10 characters in the file
print(text)
fo.close()

fo = open("test2.txt", "w+") ### Creates for us the file if its not yet there
fo.write("This is my new file")
fo.close()


##########################################################
#######################  CLASSES & OBJECTS  ##############
##########################################################
class Person:
    __name = "" ### The double underscore "__" indicates that this is a private attribute
    __email = "" ### The double underscore "__" indicates that this is a private attribute

    def __init__(self, name, email): ### This is a constructor
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def toString(self): ### Formating strings
        return "{} can be contacted at {}".format(self.__name, self.__email)


class Customer(Person): ### This means that the class Customer inherits class Person
    __balance = 0 ### Setting the default balance to zero "0"

    def __init__(self, name, email, balance):
        super(Customer, self).__init__(name, email) ### The constructor of this class
        self.__name = name
        self.__email = email
        self.__balance = balance

    def set_balance(self, balance):
        self.__balance = balance

    def toString(self):
        return "{} has a balance of {} and can be contacted at {}".format(self.__name, self.__balance, self.__email)

""" ### Using the classes methods to create an object. For this to work, the class should not have a constructor
mike = Person()
mike.set_name("Mwanje Mike")
mike.set_email("mwanjemike767@gmail.com")
print("His name is:", mike.get_name())
print("And his email is:",mike.get_email())
"""
### Using the constructor to create an object
nyika = Person("Nyika Meleby Jino Bambino", "nyikameleby@gmail.com")
print(nyika.get_name())
print(nyika.get_email())

print(nyika.toString()) ### Printing the formmated string

john = Customer("John Wick", "johnwick@gmail.com", 10000)
print("\n",john.toString())

john.set_balance(4000) ### Updating john's balance
print("\n",john.toString())
