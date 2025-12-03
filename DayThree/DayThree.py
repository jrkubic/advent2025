# --- Day 3: Lobby ---

# You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

# "Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

# You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

# "But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

# There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:

# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111

# The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

# You'll need to find the largest possible joltage each bank can produce. In the above example:

#     In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
#     In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
#     In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
#     In 818181911112111, the largest joltage you can produce is 92.

# The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

# There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?


from os import path
import sys
import re
import pytest


# We map input -> expected result (True for repeat, False for clean)
test_data = [
    ("987654321111111", 98),   
    ("811111111111119", 89),    
    ("234234234234278", 78),    
    ("818181911112111", 92),  
]

test_data_pt2 = [
    ("987654321111111", 987654321111),   
    ("811111111111119", 811111111119),    
    ("234234234234278", 434234234278),    
    ("818181911112111", 888911112111),  
]
# Part two, not happy with myself. Needed too much help to get here. 
def DayThreePartTwo(numRange):
    resultVal = []
    droppedAmount = len(numRange) - 12
    currMax = 0
    for i in numRange:
        while droppedAmount > 0 and resultVal and i > resultVal[-1]:
            resultVal.pop()
            droppedAmount -= 1
        resultVal.append(i)

    result = "".join(resultVal[:12])
    return int(result)
            # if (numRange[i] < numRange[i + 1]):
                 
        # for j in range(i + 1, len(numRange)):          
        #     number = int(numRange[i] + numRange[j])
        #     # print(number)
        #     if number > currMax:
        #         currMax = number
                # resultVal = resultVal + str(currMax)
    # print("result:", str(resultVal))
    # print("currMax:", currMax)
    # result = int(numRange) - int(currMax)
    # return result

# Part one, happy with myself. Could've done better and faster
def DayThree(numRange):
    currMax = 0
    for i in range(len(numRange) - 1):          
        for j in range(i + 1, len(numRange)):          
            number = int(numRange[i] + numRange[j])
            if number > currMax:
                currMax = number
    print(currMax)
    return currMax
      
@pytest.mark.parametrize("range, expected", test_data_pt2)
def test_repeating_groups(range, expected):
    result = DayThreePartTwo(range)
    print(result)
    assert result == expected, f"Failed on {range}"

if __name__ == '__main__':
    with open(path.join(path.dirname(__file__), "input.txt")) as f:  
        result = 0
        for line in f:
#             # print("Line", line)
            result += DayThreePartTwo(str(line.strip()))
            # result += result
            print(result)
        