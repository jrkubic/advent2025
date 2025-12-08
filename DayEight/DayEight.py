# --- Day 8: Playground ---

# Equipped with a new understanding of teleporter maintenance, you confidently step onto the repaired teleporter pad.

# You rematerialize on an unfamiliar teleporter pad and find yourself in a vast underground space which contains a giant playground!

# Across the playground, a group of Elves are working on setting up an ambitious Christmas decoration project. Through careful rigging, they have suspended a large number of small electrical junction boxes.

# Their plan is to connect the junction boxes with long strings of lights. Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes.

# The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

# For example:
from os import path
import sys
import re
import pytest
import numpy


def DayEightPartOne(numRange):
    ...
    return validCount
            

if __name__ == '__main__':
    invalidCount = 0
    validCount = 0
    data = []

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        for row in f:
            data.append([str(x) for x in row.strip()])

    result = DayEightPartOne(data)

    print(result)
        
