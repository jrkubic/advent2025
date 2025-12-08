# --- Day 7: Laboratories ---

# You thank the cephalopods for the help and exit the trash compactor, finding yourself in the familiar halls of a North Pole research wing.

# Based on the large sign that says "teleporter hub", they seem to be researching teleportation; you can't help but try it for yourself and step onto the large yellow teleporter pad.

# Suddenly, you find yourself in an unfamiliar room! The room has no doors; the only way out is the teleporter. Unfortunately, the teleporter seems to be leaking magic smoke.

# Since this is a teleporter lab, there are lots of spare parts, manuals, and diagnostic equipment lying around. After connecting one of the diagnostic tools, it helpfully displays error code 0H-N0, which apparently means that there's an issue with one of the tachyon manifolds.

# You quickly locate a diagram of the tachyon manifold (your puzzle input). A tachyon beam enters the manifold at the location marked S; tachyon beams always move downward. Tachyon beams pass freely through empty space (.). However, if a tachyon beam encounters a splitter (^), the beam is stopped; instead, a new tachyon beam continues from the immediate left and from the immediate right of the splitter.

#Very happy with today, only help needed was on regex bc I don't got it like that.
from os import path
import sys
import re
import pytest
import numpy


def DaySevenPartOne(numRange):
    invalidCount = 0
    validCount = 0
    ogMatrix = [row[:] for row in numRange]

    for i in range(len(list(numRange))):
        for j in range(len(list(numRange[0]))):
            if (ogMatrix[i][j] == 'S'):
                numRange[i + 1][j] = '|'
            elif (numRange[i][j] == '|'):
                if 0 <= i + 1 < len(numRange) and 0 <= j + 1 < len(numRange[0]):
                    if(ogMatrix[i + 1][j] == "^"):
                        numRange[i + 1][j + 1] = '|'
                        numRange[i + 1][j - 1] = '|'
                    else:
                        numRange[i + 1][j] = '|'
            elif (ogMatrix[i][j] == '^'):
                print(ogMatrix[i][j])
                if (numRange[i-1][j] == '|'):
                    validCount += 1
                    if 0 <= i +1 < len(numRange) and 0 <= j < len(numRange[0]):
                        numRange[i][j + 1] == '|'
                        numRange[i][j - 1] == '|'
               
    return validCount


if __name__ == '__main__':
    invalidCount = 0
    validCount = 0
    data = []

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        for row in f:
            data.append([str(x) for x in row.strip()])

    result = DaySevenPartOne(data)


    print(result)
        
