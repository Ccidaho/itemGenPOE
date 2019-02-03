"""
Script Version - 0.03

Script Purpose:
    This script generates items from the popular
    MMO Path of Exile, these items will have
    both prefixes and affixes.

Possible Items:
    Blank Amulet - added (0.01)

#1 - The Amulet Class
    #1.0 - The Variables
    #1.1 - The Meat

#2 - The Property Generation
    #2.0 - The Variables
    #2.1 - The Cases
    #2.2 - The Average Return

#3 - The Table Interpreter
    #3.0 - The Variables
    #3.1 - The File Interpreter
    #3.2 - The String/Line Interpreter
    #3.3 - The Conditionals




#1 - Amulet Class
    Amulet Class is a conduit through which
    many different unique amulets can be generated.



#1.0 - The Variables

'suffixes = []
prefixes = []'
    Both of these serve the purpose of holding
    specific unique prefixes or suffixes, due
    to the way that both of the 'add' functions
    are structured the max of both of these
    is three.




#1.1 - The Meat

'def __init__(self, name):'
    The __init__ function is called at the
    creation of an instance of a class, and the
    arguments presented within are what's needed
    to create the class. The exception to that
    being the 'self' argument which is always passed
    into every sub-function of any class.

'self.Name = name'
    All this does is set the 'Name' attribute
    of the amulet, to the name passed through
    during it's creation.

'def add_Prefix(self):
    if(len(self.suffixes) !=3 ):
        self.prefixes.append(propGen("Suffix"))'
    This line appears somewhat complicated on the
    surface, but when broken down is relatively simple.
    When the function add_Prefix() is called you
    first check whether or not self.suffixes is
    at a length of three, and finally append the output
    of the 'propGen' function with the argument of
    Prefix into the prefixes array.






#3 - Table Interpreter
    This function will find the array that is
    being called for inside of a text file,
    intrepret it, and return it. This relies
    on the 're' library, which allows python
    to use regex.



#3.0 - Variables

'arrayName'
    This represents the array that you're
    looking for when you call the function.

'line = mainFile.readline()'
    This grabs the next line in the file,
    and then sets it as the 'line' variable
    which can then be interpreted as a string.

'rightBracketFinder'
    This is a variable that attempts to find
    the left bracket that ends the specific
    array.

'returnArray'
    Represents the array that is returned
    after the function is run.

'strTester'
    This is used in the conditionals
    section in order to determine whether or
    not a given string can be  transformed
    into an integer.

'strHolder'
    Holds the current string.



#3.1 - File Interpreter

This section deals with extremely basic file
handling and interpretation.

'with open(filepath) as mainFile:'
    This is a way of telling Python to open your
    selected file, set by filepath, and then
    read it or write it.

'while line:'
    This checks if the 'line' variable
    has something inside of it.



#3.2 - String/Line Interpreter

This section handles the very basics of reading
lines, and when the script should be doing it.

'if(line.find(arrayName) != -1) or (rightBracketFinder == 1)'
    In short this line checks if the name of the array
    you're looking for exists on the given line, or
    if 'rightBracketFinder' has been flipped to the on state.
    This is here to prevent every line from being read and
    added to the 'returnArray' array.
    #Under a normal run this would first find the name of the
    array, flip 'rightBracketFinder' to the on state, examine
    array values until rightBracketFinder was present in the
    given line, and then never trigger again.

'for x in range (line.find("[")+1,len(line))'
    All this does is run through the current 'line'
    variable, with x representing the current position,
    starting at the line's first instance of the left
    bracket and runs until it x reaches the end of the line.
    #When no left bracket is found, python sets it to -1.



#3.3 - Conditionals

This is the real meat of the script, deciding
what is considered data within the array and how
to deal with it once it's been found.

'if(line[x] != ","):
    strHolder += line[x]
else:'
    This is a simple way of telling the script
    that once a comma is found, stop adding to
    the script and then preform actions necessary
    to append the correct data to the array.

'if(line.find("]") != -1):
    rightBracketFinder = 0'
    This is a way of reseting rightBracketFinder
    to the off position, so that when running
    through the program the first if statement
    won't trigger.

'if(re.search("[A-Za-z]", strHolder) == None)'
    This if statement uses the regex library
    're' to cehck if a given string could be
    turned into an integer.

"""
import re
import random



class Amulet:
    suffixes = []
    prefixes = []
    def __init__(self, name):
        self.Name = name

    def add_Prefix(self):
        if(len(self.prefixes) != 3):
            self.prefixes.append(propGen("Prefix"))

    def add_Suffix(self):
        if(len(self.suffixes) != 3):
            self.suffixes.append(propGen("Suffix"))



def propGen(fix):

    tableType = arrayFinder(str(fix+"Table"))
    randomTableNumber = random.randint(0, len(tableType)-1)
    tableGenerate = tableType[randomTableNumber]
    print(tableGenerate)
    table = arrayFinder(tableGenerate+"Table")
    print(table)
    dangerTable = arrayFinder("dangerTable")
    for x in range (len(dangerTable)):

        if(dangerTable[x] == tableGenerate):
            randomValue = random.randint(1, len(table)-1)
            if(x <= 3):
                while(randomValue%2 == 0):
                    randomValue = random.randint(1, len(table)-1)
                randomRangeOne = random.randint(table[randomValue-1],
                                                table[randomValue]-1)
                tableTwo = arrayFinder("two"+tableGenerate[3:])
                randomRangeTwo = random.randint(tableTwo[randomValue-1],
                                                tableTwo[randomValue]-1)
                nameTable = arrayFinder("attackNamesTable")
                return(randomTableNumber,
                       nameTable[x].format(randomRangeOne,
                                           randomRangeTwo))
            if(x > 7):
                print("Triples")
            else:
                print("Leech")
    randomValue = random.randint(2, len(table)-1)
    randomRangeOne = random.randint(table[randomValue-1],
                                    table[randomValue]-1)
    print(table[0])
    return(table[0].format(randomRangeOne))


def arrayFinder(arrayName):

    filepath = "itemArray.txt"
    with open(filepath) as mainFile:
        line = mainFile.readline()
        rightBracketFinder = 0
        returnArray = []

        while line:
            strHolder = ""
            if(line.find(arrayName) != -1) or (rightBracketFinder == 1):
                rightBracketFinder = 1
                for x in range (line.find("[")+1, len(line)):
                    if(line[x] != ",") and (line[x] != "]"):
                        strHolder += line[x]
                    else:
                        strHolder = strHolder.strip(' "')
                        if(line.find("]") != -1):
                            rightBracketFinder = 0
                        if(re.search("[A-Za-z]", strHolder) == None):
                            strHolder = int(strHolder)
                        returnArray.append(strHolder)
                        strHolder = ""
            line = mainFile.readline()
        return(returnArray)
blankAmulet = Amulet("Test Amulet")
blankAmulet.add_Prefix()
print(blankAmulet.prefixes)
