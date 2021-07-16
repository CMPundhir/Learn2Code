'''
Q. What is File Handling?
Ans. 1. File handling is an important part of any web application.
2. Python has several functions for creating, reading, updating, and deleting files.
 - >CRUD


The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.


There are four different methods (modes) for opening a file:

1. "r" - Read - Default value. Opens a file for reading, error if the file does not exist

2. "a" - Append - Opens a file for appending, creates the file if it does not exist

3. "w" - Write - Opens a file for writing, creates the file if it does not exist

4. "x" - Create - Creates the specified file, returns an error if the file exists

5. "t" - Text - Default value. Text mode

6. "b" - Binary - Binary mode (e.g. images)
'''

import json



fileFollowers = open("cm_followers.json", 'r')
print(type(fileFollowers))

follwers = fileFollowers.read()

print(type(follwers))

follwersList = json.loads(follwers)

print("count: ",len(follwersList))

firstFollower = follwersList[0]

print("type of follwersList : ", type(follwersList))
print("type of firstFollower object : ", type(firstFollower))

print("first follower Name : ", firstFollower['login'])


'''
How json is parsed in Python

JSON array converts into List
Json Object converts into Dictionary

'''

