


"""
Chapter 10
Files we might deal with as QA engineer

- Yaml ( similar to dictionaries)
- csv
- text (fixed width)
- xml
- json

Opening in Python:
open('C:/dev/basics/data/somefile) as alias_name:
    # some code to do with file
    # read line by line
    alias_name.exit or close the file

with open('C:/dev/basics/data/somefile) as alias_name:
    # some code to do with file
    # read line by line
    #it will close the file and clean the memory


windows C:\dev\basics\data\
Linux/mac  C:\\dev\\basics\\data\\ OR C:/dev/basics/data/
"""

import yaml    # specific library to handle yaml files





myfile = "../data/names.txt"

def read_file_1(filepath):
    with open(filepath) as names:
        #print(names.read())
        print(names.readline()) # reads the current line
        print(names.readline()) # reads the next line
        print(names.readlines()) # creates the list from the rest of the lines
        print(names.name) # returns the name of the file

def read_file_lines(filepath):
    with open(filepath) as data:
        for line in data.readlines():
            print('line value: ', line, end="")

#read_file_lines(myfile)
read_file_lines(myfile)

