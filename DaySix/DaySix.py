##-- Day 6: Trash Compactor ---

# After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

# A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

# As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

# Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

# However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

from os import path
import re
import pytest
import numpy as np
import pandas as pd


def daySixPartOne (numRange):
    df = pd.DataFrame(numRange, columns=['range_str'])
    quickSplitRanges = df['range_str'].str.split(expand=True)
    total = 0
    for column in quickSplitRanges:
        columnTotal = 0
        operator = quickSplitRanges[column][-1:]
        if (operator.values == "+" ):
            columnTotal = quickSplitRanges[column][:-1].astype('Int64').sum()
        elif (operator.values == "*" ):
            columnTotal = quickSplitRanges[column][:-1].astype('Int64').prod()
        total += columnTotal
    return total

def daySixPartTwo (numRange):
    df = pd.DataFrame(numRange, columns=['range_str'])
    quickSplitRanges = pd.DataFrame(df['range_str'].astype(str).apply(list).tolist())

    columnTotal = 0
    total = 0
    for column in quickSplitRanges:
        
        if (quickSplitRanges[column][-1:].any()):
            operator = quickSplitRanges[column][-1:]
        
        if (operator.values == "+" ):
            print(int(quickSplitRanges[column][:-1].sum()))
            columnTotal += int(quickSplitRanges[column][:-1].sum())
        elif (operator.values == "*" ):
            columnTotal *= int(quickSplitRanges[column][:-1].sum())

    return total
   
if __name__ == '__main__':
    data = []
    ranges = []
    ids = []
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        result = daySixPartTwo(f)
    # print(result)

        