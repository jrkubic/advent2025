##
##
##

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
   
if __name__ == '__main__':
    data = []
    ranges = []
    ids = []
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        result = daySixPartOne(f)
    
    print(result)

        