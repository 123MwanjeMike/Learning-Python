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
########### CONDITIONAL STATEMENTS ########################
##########################################################
