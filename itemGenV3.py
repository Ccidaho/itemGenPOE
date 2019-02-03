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



#2 - Property Generation
    This function will take the input of
    'Prefix' or 'Suffix', generate a random
    prefix or suffix array, and transform it
    into actual data that can be handled
    by the Amulet Class.



#2.0 - Variables

'tableType = arrayFinder(str(fix+"Table"))'
    In this variable we call the arrayFinder
    function, aka #3, with our newly assmbled
    string which is either the Prefix or Suffix
    table.

'randomTableNumber = random.randint(0, len(tableType)-1)'
    This generates a random piece of data that
    can be used to call that array once we combine
    it with "Table" and plug it into arrayFinder

'tableGenerate = tableType[randomTableNumber]'
    This is a way of storing the given data's
    position within the Prefix or Suffix table,
    and it will be used in future updates to
    ensure no double Prefixes or Suffixes.

'table = arrayFinder(tableGenerate+"Table")'
    This sets the 'table' variable to that of
    the generated table run through the array
    finder.

'dangerTable = arrayFinder("dangerTable")'
    dangerTable is an array stored within
    the itemArray.txt file, and is where
    all of the edge cases are stored so
    we can deal with them properly.




#2.1 - Cases

'for x in range (len(dangerTable)):
    if(dangerTable[x] == tableGenerate):'
    All this does is run through the variable
    dangerTable and check if the table that
    was generated matches.

'randomValue = random.randint(1, len(table)-1)'
    This will generate a random value for use
    of all of the edge cases.
    #NOTE - The reasoning as to it starts at 1
            instead of zero has to deal with how
            the specific properties are generated.

'randomRangeOne = random.randint(table[randomValue-1],
                                 table[randomValue]-1)'
    This is the crux of how we generate properties.
    For the first roll range you take the randomValue,
    subtract one, and then plug it into the table.
    For the secon droll range you take the randomValue
    plug it into the table, and then subtract one from it.
    For instance:
    Expected Output -
        randomRangeOne = random.randint(table[0],table[1]-1)
        or
        randomRangeOne = random.randint(1,(3)-1)
        or
        randomRangeOne = random.randint(1,2)

'nameTable = arrayFinder("attackNamesTable")'
    Under normal circumstances the given array
    would have the necessary output stored
    at position zero in the table, however
    with this edge case all names have been
    stored inside of the attackNamesTable.

'return(nameTable[x].format(randomRangeOne, randomRangeTwo))'
    We use the afformentioned x that has been
    keeping track of which edge cases we're dealing
    with to generate any one of four names from
    the name table, this can be done because
    the names in the dangerTable correlate
    to the names in the nameTable.
    After the output is selected we use the format
    function to replace all instances of {}
    with our data, in this case our data is
    randomRangeOne, and randomRangeTwo.



#2.2 - Average Return

'randomValue = random.randint(2, len(table-1))'
    This will generate a random value from
    the given table which is not an edge case,
    the data of the table starts at position one
    but because of the way that data is generated
    we need an output higher than that of the first
    data position.

'return(table[0].format(randomRangeOne))'
    This is fairly simple, first we take
    the zero position in the table, and then
    plug randomRangeOne into it's {}, and then
    return it.

'randomRangeOne = random.randint(table[randomValue-1],
                                 table[randomValue]-1)'
    This is the crux of how we generate properties.
    For the first roll range you take the randomValue,
    subtract one, and then plug it into the table.
    For the secon droll range you take the randomValue
    plug it into the table, and then subtract one from it.
    For instance:
    Expected Output -
        randomRangeOne = random.randint(table[0],table[1]-1)
        or
        randomRangeOne = random.randint(1,(3)-1)
        or
        randomRangeOne = random.randint(1,2)



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
