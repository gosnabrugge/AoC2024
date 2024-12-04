# -*- coding: utf-8 -*-
"""
Advent of Code day 1 script
"""
import numpy as np

#### Part 1 ####
# readout ID numbers from txt document
leftIDs= np.array([])
rightIDs = np.array([])
for line in open('input.txt'):
    numbersRow = line.split("  ")
    leftIDs = np.append(leftIDs,int(numbersRow[0]))
    rightIDs = np.append(rightIDs,int(numbersRow[1]))

# sort lists in ascending order
leftIDsSorted = np.sort(leftIDs)
rightIDsSorted = np.sort(rightIDs)

# compute distance between matching list entries
distIDs = int(np.sum(np.abs(leftIDsSorted - rightIDsSorted)))

print(distIDs)

#### Part 2 ####
# check number of occurences of left ID number in right list
simScore = int(0)
for leftID in leftIDs:
    nMatches = sum(rightIDs == leftID)
    simScore += int(leftID*nMatches)

print(simScore)