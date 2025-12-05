##
##
##

from os import path
import sys
import re
import pytest

def PartOne(numRange):
    invalidCount = 0
    validCount = 0
    start = int(numRange.split("-")[0])
    end = int(numRange.split("-")[1])
    for i in range(start, end+1):
        print(i)
        if (bool(re.compile(r'^(.+)\1+$').fullmatch(str(i)))):
            print("INVALID")
            invalidCount += 1
        else:
            print("VALID")
            validCount += 1
    print("invalidCount: ", invalidCount)
    return invalidCount


if __name__ == '__main__':
    invalidCount = 0
    validCount = 0
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        for instruction in f:                
            ListSplitByCommas = instruction.split(",")
            for numRange in ListSplitByCommas:
                start = int(numRange.split("-")[0])
                end = int(numRange.split("-")[1])
                for i in range(start, end + 1):
                    if (bool(re.compile(r'^(.+)\1+$').fullmatch(str(i)))):
                        invalidCount += i
                    else:
                        validCount += 1

    print(invalidCount)
        
# @pytest.mark.parametrize("range, expected", test_data_pt2)
# def test_repeating_groups(range, expected):
#     result = PartOne(range)
#     # print(result)
#     assert result == expected, f"Failed on {range}"

# # if __name__ == '__main__':
     

# #         PartOne(f)
        