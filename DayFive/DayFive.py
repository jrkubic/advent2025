# -- Day 4: Printing Department ---

# You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

# Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

# "Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

# If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

# The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

# For example:

# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.

# The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

# In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.

# Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?

# Your puzzle answer was 1527.
# --- Part Two ---

# Now, the Elves just need help accessing as much of the paper as they can.

# Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

# Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

# Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

# Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?

# Your puzzle answer was 8690.

from os import path
import sys
# print(sys.maxsize)
import re
import pytest
import numpy as np
import pandas as pd


BATCH_SIZE = 10_000_000

def partFourAddFreshID (numRange, freshArray, idList) :
    resultArray = []
    # print("In partFourAddFreshID...")
    for row in numRange:
        start = int(row.split("-")[0])
        end = int(row.split("-")[1])
        for id in idList:
            if int(id) >= start and int(id) <= end and int(id) not in resultArray:
                # print("FRESH", id)
                resultArray.append(int(id))
        # for i in range(start, end+1):
        #     resultArray.append(i)
    # print("ResultArray", resultArray)
    return resultArray

def partFourPartTwo (numRange) :
    resultAmount = 0
    freshValues = []
    # print("In partFourAddFreshID...")
    #new strat, lets be smart
    df = pd.DataFrame(numRange, columns=['range_str'])
    quickSplitRanges = df['range_str'].str.split('-', expand=True).astype(np.int64)
    # print("quickSplitRanges[0].values: ", quickSplitRanges[0].values)
    # print(quickSplitRanges[0])
    allStarts = quickSplitRanges[0].values
    allEnds = quickSplitRanges[1].values + 1

    sort_idxs = np.argsort(allStarts)

    merged_starts = []
    merged_ends = []

    sortedStarts = allStarts[sort_idxs]
    sortedEnds = allEnds[sort_idxs]
    if len(sortedStarts) > 0:
        curr_s = sortedStarts[0]
        curr_e = sortedEnds[0]
        for i in range(1, len(sortedStarts)):
                next_s = sortedStarts[i]
                next_e = sortedEnds[i]

                if next_s < curr_e: 
                    curr_e = max(curr_e, next_e)
                else:
                    merged_starts.append(curr_s)
                    merged_ends.append(curr_e)
                    curr_s = next_s
                    curr_e = next_e
                    
        merged_starts.append(curr_s)
        merged_ends.append(curr_e)

        total_count = np.sum(np.array(merged_ends) - np.array(merged_starts))
    return total_count
    # print(sort_idxs)
    # for starts, ends in zip(allStarts, allEnds):
    #     # pandas and  numpy wasnt enough on their own. Trying batch size cap.
    #     for batch_s in range(starts, ends, BATCH_SIZE):
    #         batch_e = min(batch_s + BATCH_SIZE, ends)

    #         chunk = np.arange(batch_s, batch_e)            
    #         return list(set(chunk))

    # for row in numRange:
    #     start = int(row.split("-")[0])
    #     end = int(row.split("-")[1])
    #     difference = int(end) - int(start)
    #     # if (range(start, end)):
    #         # if range(start, end) in freshValues:
    #     # freshValues.extend(range(start, end + 1))
    #     np.array(freshValues)
        
    #     for x in range(start, end + 1):
    #         ...
            #  freshValues.append(x)
        # for id in idList:
        # for i in difference:
        #     count += 1
        # resultAmount += (difference + 1)
    # list(set(freshValues))
    # print(len((freshValues)))
    # print(len(list(set(freshValues))))

    # return len(list(set(freshValues)))
        # while start != end:
        #     if start not in resultArray:
        #         print("FRESH ", start)
        #         resultArray.append(start)
        #     start += 1
        
        # if int(id) not in resultArray:
        #     print("FRESH", id)
        #     resultArray.append(int(id))
    # return resultArray

def partFourRanges(numRange):
    # print("In partFourRanges...")

    freshFruitRange = []
    for row in numRange:
        if "-" in row:
            freshFruitRange.append(row)
    return freshFruitRange

def partFourIds(numRange):
    # print("In partFourIds...")
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
