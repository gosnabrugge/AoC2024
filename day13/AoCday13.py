# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day 13 script
author: g.osnabrugge
"""
import numpy as np
# from collections import defaultdict
import time
t0 = time.time()

#%%# helper functions #%%#
def loadData(inputFile):
    # load raw data in string format (line by line)
    with open(inputFile) as file:
        lines = [line.rstrip() for line in file]
    
    return lines

def solveCraneMachine(mLines, part2):
    # parse string data into system of equations and find solution
    # extract button-A data
    startInd = mLines[0].find('X+')+2
    stopInd = mLines[0].find(',')
    a = int(mLines[0][startInd:stopInd])
    startInd = mLines[0].find('Y+')+2
    c = int(mLines[0][startInd::])
    
    # extract button-B data
    startInd = mLines[1].find('X+')+2
    stopInd = mLines[1].find(',')
    b = int(mLines[1][startInd:stopInd])
    startInd = mLines[1].find('Y+')+2
    d = int(mLines[1][startInd::])
    
    # extract prize data
    startInd = mLines[2].find('X=')+2
    stopInd = mLines[2].find(',')
    s1 = int(mLines[2][startInd:stopInd])
    startInd = mLines[2].find('Y=')+2
    s2 = int(mLines[2][startInd::])
    if part2:
        s1 += 10000000000000
        s2 += 10000000000000
    
    # solve system of equations and check if solution is a positive and round number of steps in X and Y
    x1 = round(1/(a*d-b*c)*(d*s1  - b*s2))
    x2 = round(1/(a*d-b*c)*(-c*s1 + a*s2))
    sx1 = a*int(x1)+b*int(x2)
    sx2 = c*int(x1)+d*int(x2)
    
    if (sx1 == s1 and sx2 == s2) and (x1>=0 and x2>=0):
        return int(3*x1 + x2) # number of tokens needed for solution
    else: return 0
        
#%%# readout puzzle input file #%%#
lines = loadData('input.txt')

#%%%# Part 1 & 2 #%%#
resultsPart1 = 0
resultsPart2 = 0
nMachines = int(np.ceil(len(lines)/4))

for iMachine in range(nMachines):
    mLines = lines[4*iMachine:4*iMachine+3]   # input 
    resultsPart1 += solveCraneMachine(mLines, False)
    resultsPart2 += solveCraneMachine(mLines, True)

#%%%# print results #%%#
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {time.time()-t0:.3f} sec')