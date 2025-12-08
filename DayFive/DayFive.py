# --- Day 5: Cafeteria ---

# As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

# You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

# "If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

# The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

# The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:



# The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

# The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

# So, in this example, 3 of the available ingredient IDs are fresh.

# Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?

# Your puzzle answer was 821.
# --- Part Two ---

# The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

# So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

# Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:


# The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

# Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

# Your puzzle answer was 344771884978261.

# Both parts of this puzzle are complete! They provide two gold stars: **

# At this point, you should return to your Advent calendar and try another puzzle.

from os import path
import sys
# print(sys.maxsize)
import re
import pytest
import numpy as np
import pandas as pd


BATCH_SIZE = 10_000_000

def partFourAddFreshID (numRange, freshArray, idList):
    resultArray = []
    # print("In partFourAddFreshID...")
    for row in numRange:
        start = int(row.split("-")[0])
        end = int(row.split("-")[1])
        for id in idList:
            if int(id) >= start and int(id) <= end and int(id) not in resultArray:
                resultArray.append(int(id))
    return resultArray

def partFourPartTwo (numRange):

    # new strat, lets be smart
    df = pd.DataFrame(numRange, columns=['range_str'])
    quickSplitRanges = df['range_str'].str.split('-', expand=True).astype(np.int64)

    allStarts = quickSplitRanges[0].values
    allEnds = quickSplitRanges[1].values + 1

    sortIds = np.argsort(allStarts)

    mergedStarts = []
    mergedEnds = []

    sortedStarts = allStarts[sortIds]
    sortedEnds = allEnds[sortIds]
    if len(sortedStarts) > 0:
        curr_s = sortedStarts[0]
        curr_e = sortedEnds[0]
        for i in range(1, len(sortedStarts)):
                nextS = sortedStarts[i]
                nextE = sortedEnds[i]

                if nextS < curr_e: 
                    curr_e = max(curr_e, nextE)
                else:
                    mergedStarts.append(curr_s)
                    mergedEnds.append(curr_e)
                    curr_s = nextS
                    curr_e = nextE
                    
        mergedStarts.append(curr_s)
        mergedEnds.append(curr_e)

        totalCount = np.sum(np.array(mergedEnds) - np.array(mergedStarts))
    return totalCount
   
def partFourRanges(numRange):

    freshFruitRange = []
    for row in numRange:
        if "-" in row:
            freshFruitRange.append(row)
    return freshFruitRange

def partFourIds(numRange):
    freshFruitIds = []
    for row in numRange:
        if "-" not in row and row:
            freshFruitIds.append(row)
    return freshFruitIds

if __name__ == '__main__':
    data = []
    ranges = []
    ids = []
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        for row in f:
            data.append(str(row).strip()) 
    ranges = partFourRanges(data)
    
    difference = partFourPartTwo(ranges)
    print(difference)
