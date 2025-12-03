
#Very happy with today, only help needed was on regex bc I don't got it like that.
from os import path
import sys
import re
import pytest


# Sample Value, Expected Value
test_data = [
    ("11-22", 2),   
    ("95-115", 1),    
    ("998-1012", 1),    
    ("1188511880-1188511890", 1),  
    ("222220-222224",      1), 
    ("1698522-1698528",   0),   
    ("446443-446449",   1),   
    ("38593856-38593862",   1),   
]

test_data_pt2 = [
    ("11-22", 2),   
    ("95-115", 2),    
    ("998-1012", 2),    
    ("1188511880-1188511890", 1),  
    ("222220-222224",      1), 
    ("1698522-1698528",   0),   
    ("446443-446449",   1),   
    ("565653-565659",   1),   
    ("824824821-824824827",   1),   
    ("2121212118-2121212124",   1),   
]

def PartFour(numRange):
    # invalidCount = 0
    # validCount = 0
    # start = int(numRange.split("-")[0])
    # end = int(numRange.split("-")[1])
    # for i in range(start, end+1):
    #     print(i)
    #     if (bool(re.compile(r'^(.+)\1+$').fullmatch(str(i)))):
    #         print("INVALID")
    #         invalidCount += 1
    #     else:
    #         print("VALID")
    #         validCount += 1
    # print("invalidCount: ", invalidCount)
    # return invalidCount
    ...



if __name__ == '__main__':
    invalidCount = 0
    validCount = 0
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        ...
        # for instruction in f:                
        #     ListSplitByCommas = instruction.split(",")
        #     for numRange in ListSplitByCommas:
        #         start = int(numRange.split("-")[0])
        #         end = int(numRange.split("-")[1])
        #         for i in range(start, end + 1):
        #             if (bool(re.compile(r'^(.+)\1+$').fullmatch(str(i)))):
        #                 invalidCount += i
        #             else:
        #                 validCount += 1

    # print(invalidCount)
        


# @pytest.mark.parametrize("range, expected", test_data_pt2)
# def test_repeating_groups(range, expected):
#     result = PartOne(range)
#     # print(result)
#     assert result == expected, f"Failed on {range}"
