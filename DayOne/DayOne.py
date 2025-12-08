 
# # --- Day 1: Secret Entrance ---
# # The Elves have good news and bad news.
# # The good news is that they've discovered project management! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time.
# # The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole!
# # To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.
# # Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# # You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:
# # "Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."
# # The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.
# # The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.
# # So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.
# # Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.
# # So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.
# # The dial starts by pointing at 50.
# # You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
# # For example, suppose the attached document contained the following rotations:


# # Following these rotations would cause the dial to move as follows:


# # Because the dial points at 0 a total of three times during this process, the password in this example is 3.
# # Analyze the rotations in your attached document. What's the actual password to open the door?
# # To play, please identify yourself via one of these services:
# # [GitHub] [Google] [Twitter] [Reddit] - [How Does Auth Work?]


from os import path
import sys

# startPosition = 50


# #PART 2
# def rotateCalcCountZeros(instruction, distance, lastPosition, counter):
#     if (instruction == "L"):
#         calculatedPosition = (lastPosition - distance) % 100
#         if lastPosition < distance:
#             counter += 1 
        
#     elif (instruction == "R"):
#         calculatedPosition = (lastPosition + distance) % 100
#         if lastPosition > distance or distance == 0:
#             counter += 1
        
#     # print(counter)
#     return counter

# # PART 1
# def rotateCalc(instruction, distance, lastPosition):
#     curr_pos = startPosition
#     counter = 0
#     if (instruction == "L"):
#         calculatedPosition = (lastPosition - distance) % 100
#         calculated_zeros = (lastPosition - distance) // 100
        
#     elif (instruction == "R"):
#         calculatedPosition = (lastPosition + distance) % 100
#         calculated_zeros = (lastPosition - distance) // 100
#         if curr_pos == 0:
#             # Starting at 0: only count complete loops (not the starting position)
#             counter += distance // 100
#         elif distance > curr_pos:
#             # We cross 0 at least once during the CCW rotation
#             counter += ((distance - curr_pos - 1) // 100) + 1
#             # If we also END on 0, count that final landing
#             if calculatedPosition == 0:
#                 counter += 1
#         elif distance == curr_pos:
#             # We land exactly on 0
#             counter += 1
#         # else: clicks < curr_pos, we don't reach 0
#         counter += abs()
#         curr_pos = calculatedPosition
        
#     print(abs(calculated_zeros))
#     return calculatedPosition, calculated_zeros

if __name__ == '__main__':
#     password = 0      
#     counter = 0
#     currentPosition = startPosition
    
    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        # for instruction in f:
        # for line in f:
            instructions = [(-1 if line[0] == 'L' else 1, int(line[1:])) for line in f]

            acc = 0
            x = 50

            for d, n in instructions:
                # flip
                x = (x * d) % 100

                x += n
                acc += x // 100
                x %= 100

                # unflip
                x = (x * d) % 100

            print(acc)
