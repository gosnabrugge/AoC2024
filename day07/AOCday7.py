# -*- coding: utf-8 -*-
"""
Advent of Code day 7 script
author: g.osnabrugge
"""
import numpy as np
import time

#%%# helper functions #%%#
def solveEq(leftPart,rightPart, nTypes):
    eqSolvable = False
    nOps = len(rightPart)-1 # number of operators in equation
    nCombs = nTypes**nOps   # number of possible combinations
    
    for i in range(nCombs):
        # generate operator flags (binary or ternary)
        opsFlags = np.base_repr(i, nTypes)
        opsFlags = '0'*(nOps-len(opsFlags))+opsFlags # pad string to nOps length

        result = rightPart[0]
        for iOps in range(0,nOps):
            if opsFlags[iOps] == '0':
                result += rightPart[iOps+1]
            elif opsFlags[iOps] == '1': # multiplication
                result *= rightPart[iOps+1]
            elif opsFlags[iOps] == '2': # concatenate (used for Part 2)
                result = int(str(result)+str(rightPart[iOps+1]))
        
        if result == leftPart:
            eqSolvable = True
            break
    
    return eqSolvable

#%%%# Part 1 & 2 #%%#
t0 = time.time()
resultsPart1 = 0
resultsPart2 = 0

for line in open('input.txt'):
    parts = line.split(': ')
    lPart = int(parts[0])
    rPart = list(map(int,parts[1].split(' ')))
    if solveEq(lPart,rPart,2):
        resultsPart1 += lPart
    
    if solveEq(lPart,rPart,3):
        resultsPart2 += lPart

# print results
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
