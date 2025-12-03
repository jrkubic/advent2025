# --- Day 2: Gift Shop ---

# You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.
# As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

# As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

# They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

# 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124

# (The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

# The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

# Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

# None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

# Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

#     11-22 has two invalid IDs, 11 and 22.
#     95-115 has one invalid ID, 99.
#     998-1012 has one invalid ID, 1010.
#     1188511880-1188511890 has one invalid ID, 1188511885.
#     222220-222224 has one invalid ID, 222222.
#     1698522-1698528 contains no invalid IDs.
#     446443-446449 has one invalid ID, 446446.
#     38593856-38593862 has one invalid ID, 38593859.
#     The rest of the ranges contain no invalid IDs.

# Adding up all the invalid IDs in this example produces 1227775554.
# What do you get if you add up all of the invalid IDs?


#Very happy with today, only help needed was on regex bc I don't got it like that.
from os import path
import sys
import re
import pytest

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
        