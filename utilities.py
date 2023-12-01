import re
import itertools as it
import pyperclip

def loadinput(path : str):
    """Gets the input"""
    inputfile = open(path)
    lines = [a.strip() for a in inputfile.readlines()]
    inputfile.close()
    return lines

def loadinputints(path: str):
    """Gets the input and casts any line that is just an integer to an integer"""
    inputfile = open(path)
    lines = [tryint(a.strip()) for a in inputfile.readlines()]
    inputfile.close()
    return lines

def tryint(val):
    """Returns casted integer if success, return original value if failed"""
    try:
        return int(val)
    except:
        return val

def getints(text: str):
    """Returns a list containing each individual integer in a string"""
    return [int(x) for x in re.findall(r"-?\d+",text)]

def makegrid(columns: int, rows: int, default):
    """Creates a grid of size specified and with the default value specified"""
    return [[default]*columns for _ in range(rows)]

def flatten(list2D: list):
    """Converts a 2D list into a 1D list"""
    return list(it.chain(*list2D))

def incrange(start: int, end: int):
    """Gets the inclusive range between two ints. Can also generate in reverse"""
    if end>=start:
        return range(start,end+1)
    else:
        return range(start,end-1,-1)

def removechars(text: str, charsToRemove: str):
    """Returns 'text' with any characters that appear in 'charsToRemove' removed"""
    return re.sub("|".join(charsToRemove), "", text)

def removestringslist(text: str, stringsToRemove: list):
    """Returns 'text' with any substrings that appear in the 'stringsToRemove' list removed"""
    return re.sub("|".join(stringsToRemove), "", text)

def removestrings(text: str, *args: str):
    """Returns 'text' with any substrings specified removes"""
    return re.sub("|".join(args), "", text)

def splitlist(listToSplit: list, *args):
    """Returns a 2D list split by all of the values specified. The splitter values are not included in the result"""
    result = [[]]
    argset = set(args)
    for item in listToSplit:
        if item in argset:
            if result[-1]:
                result.append([])
        else:
            result[-1].append(item)
    return result

def product(nums):
    """Returns the product of all numbers in an iterable"""
    result = 1
    for num in nums:
        result *= num
    return result

def swapdict(dictionary: dict):
    """Swaps the keys and values in a dictionary. If a value is repeated then that key-value pair won't be included"""
    return dict([(val,key) for key,val in dictionary.items()])

def inbounds(val: int, bound1: int, bound2: int):
    """Checks whether a value is within some bounds. The bounds are inclusive and can be either way round"""
    return val <= max(bound1,bound2) and val >= min(bound1,bound2)

def prco(val):
    """Prints the value and copies it to clipboard"""
    print(val)
    pyperclip.copy(val)

def findalloverlap(pattern: str, string: str):
    """Same as re.findall() except that it allows for overlapping strings"""
    return re.findall("(?=("+pattern+"))",string)

u_cardinals = [(0,1),(0,-1),(1,0),(-1,0)]
u_adjacent = [(x,y) for x in incrange(-1,1) for y in incrange(-1,1) if x!=0 or y!=0]
u_digits = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
