
#Very happy with today, only help needed was on regex bc I don't got it like that.
from os import path
import sys
import re
import pytest

# Sample Value, Expected Value
# test_input = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.""".strip().splitlines()

# test_expected = 13

# test_data = [
#     (test_input, test_expected)
# ]

def partFour(numRange):
    currMax = 0
    totalX = 0

    ogMatrix = [row[:] for row in numRange]

    for i in range(len(list(numRange))):
        for j in range(len(list(numRange[0]))):
            if (ogMatrix[i][j] == '@'):
                rollCounter = 0
                
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == 0 and dx == 0:
                            continue

                        ni, nj = i + dy, j + dx
               
                        if 0 <= ni < len(numRange) and 0 <= nj < len(numRange[0]):
                            neighbor = ogMatrix[ni][nj]
                            
                            if neighbor == '@':
                                rollCounter += 1

                if rollCounter < 4:
                    numRange[i][j] = 'X'
                    totalX += 1
            elif (ogMatrix[i][j] == 'X'):
                numRange[i][j] = '.'
                # totalX -= 1

                # removedCounter = 0
            
                # for dy in range(-1, 2):
                #     for dx in range(-1, 2):
                #         if dy == 0 and dx == 0:
                #             continue

                #         ni, nj = i + dy, j + dx
               
                #         if 0 <= ni < len(numRange) and 0 <= nj < len(numRange[0]):
                #             neighbor = ogMatrix[ni][nj]
                           
                #             if neighbor == '@' or neighbor == 'X':
                #                 removedCounter += 1
                           
                # if removedCounter < 4:
                    # totalX += 1
    return numRange, totalX

        # if counter < 4:
        #     numRange[i][j] = "X"
        #     # print(numRange[i][j+1])
        #     # print(numRange[i-1][j], numRange[i][j], numRange[i+1][j])
        #     # print(numRange[i][j-1], numRange[i][j-1],numRange[i][j])
        #     totalX += 1
        #     counter = 0

            # if (i[j - 1]).contains("@"):
            #     print("j: ", j)      
            # if (i[j + 1]).contains("@"):
            #     print("j: ", j)      
                # number = int(numRange[i] + numRange[j])
                # if number > currMax:
                #     currMax = number
    # print(currMax)
    # return currMax

if __name__ == '__main__':
    invalidCount = 0
    validCount = 1
    cycleCount = 0
    total = 0
    result = []
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        for row in f:   
            result.append([str(x) for x in row.strip()])
    while validCount != 0:
        result, validCount = partFour(result)
        cycleCount += 1
        total += validCount
        print("optimalRollsRemoved :", validCount)
    print("cycleCount :", cycleCount)
    print("Total :", total)

# @pytest.mark.parametrize("range, expected", test_data)
# def test_repeating_groups(range, expected):
#     data = []
#     for row in range:
#         data.append([str(x) for x in row]) 
#     # print(data)
#     result = partFour(data)
#     assert result == expected, f"Failed on {range}"
